from typing import List
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

from models import config
from models.ClassifierInterface import ClassifierInterface
from dataset import Dataset, Article, TorchDatasetWrapper
from KMeans import KMeans

def scoresFromArticle(article: Article):
    return [
        article.clearScores.clearScore1,
        article.clearScores.clearScore2,
        article.clearScores.clearScore3,
        article.clearScores.clearScore4,
        article.clearScores.clearScore5,
        article.clearScores.clearScore6,
        article.readability.readabilityGrades.kincaid
    ]

class NieBERT(ClassifierInterface):
    nClusters = 10

    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

    @classmethod
    def getLabels(cls, dataset: Dataset):
        labels = KMeans.getLabels(dataset, scoresFromArticle)
        return labels
    
    @classmethod
    def trainFromDataset(cls, dataset: Dataset, labels: List[int], modelName: str= 'bert-base-uncased', epochs: int= 3):
        tokenizer = AutoTokenizer.from_pretrained(modelName)
        model = AutoModelForSequenceClassification.from_pretrained(modelName, num_labels=cls.nClusters)

        tDataset = TorchDatasetWrapper(dataset, labels, tokenizer)

        trainingArgs = TrainingArguments(
            per_device_train_batch_size=8,
            num_train_epochs=epochs,
            save_strategy="no"
        )
        trainer = Trainer(
            model=model,
            args=trainingArgs,
            train_dataset=tDataset
        )
        trainer.train()

        this = cls(tokenizer, model)
        return this
    
    def predict(self, article: Article):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)
        self.model.eval()

        inputs = self.tokenizer(' '.join(article.content), return_tensors='pt', padding=True, truncation=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            if outputs.logits.shape[1] == 1:
                predictions = outputs.logits.squeeze().cpu().numpy()  # regression
            else:
                predictions = torch.argmax(outputs.logits, dim=1).cpu().numpy() # classification
        return predictions.tolist()

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