from typing import List
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, WeightedRandomSampler
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments, EarlyStoppingCallback

from models import config
from models.ClassifierInterface import ClassifierInterface
from dataset import Dataset, Article, TorchDatasetWrapper
from KMeans import KMeans
from CefrCsv import CefrCsv

def scoresFromArticle(article: Article):
    scores = list(CefrCsv.countCefr(article).values())
    scores.extend([
        article.clearScores.clearScore1,
        article.clearScores.clearScore2,
        article.clearScores.clearScore3,
        article.clearScores.clearScore4,
        article.clearScores.clearScore5,
        article.clearScores.clearScore6,
        article.readability.readabilityGrades.kincaid
    ])
    return scores

class WeightedTrainer(Trainer):
    def get_train_dataloader(self):
        dataset = self.train_dataset
        weights = dataset.weights
        
        sampler = WeightedRandomSampler(weights, num_samples=len(weights), replacement=True)
        
        return DataLoader(
            dataset,
            batch_size=self.args.train_batch_size,
            sampler=sampler,
            collate_fn=self.data_collator,
            drop_last=self.args.dataloader_drop_last,
            num_workers=self.args.dataloader_num_workers,
        )
    
    def compute_loss(self, model, inputs, num_items_in_batch= None, return_outputs= False):
        weights = inputs.pop("weights", None)  # remove weights so model.forward doesn't get them
        labels = inputs["labels"]

        outputs = model(**inputs)  # no weights here
        logits = outputs.logits

        if logits.dim() > 1 and logits.size(-1) == 1:
            logits = logits.squeeze(-1)

        labels = labels.squeeze()

        loss_fct = nn.MSELoss(reduction="none")
        losses = loss_fct(logits, labels)

        if weights is not None:
            losses = losses * weights

        loss = losses.mean()
        if return_outputs:
            return loss, outputs
        else:
            return loss

class NieBert(ClassifierInterface):
    nClusters = 10

    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

    @classmethod
    def getClassificationLabels(cls, dataset: Dataset):
        labels = KMeans.getLabels(dataset, cls.nClusters, scoresFromArticle)
        return labels
    
    @classmethod
    def getRegressionLabels(cls, dataset: Dataset):
        labels = [article.clearScores.btEasiness for article in dataset]
        return labels
    
    @classmethod
    def getLabels(cls, dataset: Dataset):
        return cls.getRegressionLabels(dataset)
    
    @classmethod
    def getRegressionWeights(cls, dataset: Dataset):
        standardErrors = [article.clearScores.btStandardError for article in dataset]
        minE = min(standardErrors)
        maxE = max(standardErrors)
        weights = [
            2 - ((e - minE) / (maxE - minE)) * 1.5
            for e in standardErrors
        ]
        return weights
    
    def retrain(self, dataset: TorchDatasetWrapper, evalDataset: TorchDatasetWrapper, **kwargs):
        args = {
            'output_dir': f"../output/{self.model.config._name_or_path.replace('/','-')}",
            'logging_steps': 50,

            'num_train_epochs': 3,
            'per_device_train_batch_size': 8,
            'gradient_accumulation_steps': 2,
            'learning_rate': 1e-6,
            'weight_decay': 0.1,
            'warmup_ratio': 0.1,
            'lr_scheduler_type': 'cosine',
            
            'save_strategy': 'steps',
            'eval_strategy': 'steps',
            'load_best_model_at_end': True,
            'metric_for_best_model': 'eval_loss',
            'greater_is_better': False,
            'fp16': True,
            'dataloader_num_workers': 0,
        }
        args.update({k: kwargs[k] for k in args if k in kwargs})

        trainingArgs = TrainingArguments(**args)
        trainer = WeightedTrainer(
            model=self.model,
            args=trainingArgs,
            train_dataset=dataset,
            eval_dataset=evalDataset,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=10)]
        )
        trainer.train()

    @classmethod
    def trainFromTorchDataset(
        cls,
        dataset: TorchDatasetWrapper,
        evalDataset: TorchDatasetWrapper,
        modelName: str= 'bert-base-uncased',
        tokenizer: AutoTokenizer | None= None,
        **kwargs
    ):
        if dataset.regression:
            model = AutoModelForSequenceClassification.from_pretrained(modelName, num_labels=1)
            model.config.problem_type = "regression"
        else:
            model = AutoModelForSequenceClassification.from_pretrained(modelName, num_labels=cls.nClusters)

        try:
            model.gradient_checkpointing_enable()
        except Exception:
            pass

        args = {
            'output_dir': f"../output/{modelName.replace('/','-')}",
            'logging_steps': 50,

            'num_train_epochs': 3,
            'per_device_train_batch_size': 8,
            'gradient_accumulation_steps': 2,
            'learning_rate': 1e-5,
            'weight_decay': 0.01,
            'warmup_ratio': 0.1,
            'lr_scheduler_type': 'cosine',
            
            'save_strategy': 'steps',
            'eval_strategy': 'steps',
            'load_best_model_at_end': True,
            'metric_for_best_model': 'eval_loss',
            'greater_is_better': False,
            'fp16': True,
            'dataloader_num_workers': 0,
        }
        args.update({k: kwargs[k] for k in args if k in kwargs})

        trainingArgs = TrainingArguments(**args)
        trainer = WeightedTrainer(
            model=model,
            args=trainingArgs,
            train_dataset=dataset,
            eval_dataset=evalDataset,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=10)]
        )
        trainer.train()

        this = cls(tokenizer, model)
        return this

    @classmethod
    def trainFromDataset(
        cls,
        dataset: Dataset,
        labels: List[int|float],
        evalDataset: Dataset,
        evalLabels: List[int|float],
        weights: List[float],
        modelName: str= 'bert-base-uncased',
        splitAsSentences= False,
        tokenizer: AutoTokenizer | None= None,
        **kwargs
    ):
        if tokenizer == None:
            tokenizer = AutoTokenizer.from_pretrained(modelName)
        tDataset = TorchDatasetWrapper.fromDataset(dataset, labels, tokenizer, weights, splitAsSentences)
        tEvalDataset = TorchDatasetWrapper.fromDataset(evalDataset, evalLabels, tokenizer, splitAsSentences=splitAsSentences)

        this = cls.trainFromTorchDataset(tDataset, tEvalDataset, modelName, tokenizer, **kwargs)
        return this

    def predict(self, article: Article, splitAsSentences: bool= False):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)
        self.model.eval()

        if splitAsSentences:
            predictions = []
            for sentence in article.content:
                inputs = self.tokenizer(sentence, return_tensors='pt', padding=True, truncation=True, max_length=512)
                inputs = {k: v.to(device) for k, v in inputs.items()}

                with torch.no_grad():
                    outputs = self.model(**inputs)
                    logits = outputs.logits
                    if logits.shape[1] == 1:
                        predictions.append(logits.squeeze().item())  # regression
                    else:
                        predictions.append(torch.argmax(outputs, dim=1).item()) # classification
        else:
            inputs = self.tokenizer(' '.join(article.content), return_tensors='pt', padding=True, truncation=True, max_length=512)
            inputs = {k: v.to(device) for k, v in inputs.items()}
        
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits
                if logits.shape[1] == 1:
                    predictions = logits.squeeze().item()  # regression
                else:
                    predictions = torch.argmax(outputs, dim=1).item() # classification
        return predictions

    def predictSentence(self, sentence: str):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)
        self.model.eval()

        inputs = self.tokenizer(sentence, return_tensors='pt', padding=True, truncation=True, max_length=512)
        inputs = {k: v.to(device) for k, v in inputs.items()}
    
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            if logits.shape[1] == 1:
                predictions = logits.squeeze().item()  # regression
            else:
                predictions = torch.argmax(outputs, dim=1).item() # classification
        return predictions

    def save(self, name: str, path=config.nieBERTPath):
        self.tokenizer.save_pretrained(path(name)+'.tokenizer')
        self.model.save_pretrained(path(name)+'.model')
        return self

    @classmethod
    def load(cls, name: str, path=config.nieBERTPath):
        tokenizer = AutoTokenizer.from_pretrained(path(name)+'.tokenizer')
        model = AutoModelForSequenceClassification.from_pretrained(path(name)+'.model')
        this = cls(tokenizer, model)
        return this