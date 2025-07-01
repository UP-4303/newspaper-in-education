# A method for determining web news suitable for NIE practices

## Disclaimer

This project has been created for a research purpose. It is not meant to be used as is in any serious project.  
The goal of the project was to explore different options for determining web news suitable for NIE practices in english-speaking elementary schools.  
Also note that this was my first time dealing with AI training, evaluation and other AI-related tasks. Everything might not be optimized or used as intended, and I may have missed some things that seem obvious to the trained eye.

I should also mention this was done under the supervision of Prof. ANDO Kazuaki of Kagawa University, in Japan.  
He already did research on a similar subject, except it was for *japanese*-speaking elementary schools.  
Some methods, especially the first ones, were inspired by his.

## Compatibility

This project has only been tested with Python==3.11.12 .  
Known to be incompatible with Python<3.7, due to dictionary key order not guarantied.

## Usage

A main notebook is provided, along with the function I used for the training and evaluation of my last models.  
All models used are subject to either `ClassifierInterface` (yes, including regressors) or `VectorizerInterface`. Use their methods to chain the models.  
It is also possible to save and load trained models, via `.save(<fileName>)` and `.load(<fileName>, <...otherArgumentsMayBeNeeded>)`  
Since I was learning a lot as the project was being developed, it is severely under-documented. Don't hesitate to ask any question.

## Methods used

The full detail of the results are located in `nie_results.md`.

The first classifier used was SVM.  
I chose it as it was the main model used in the paper from Prof. Ando.  
At first, the training was done using a conversion of the Flesch grading into 10 different classes as the label.

I started by using the results from Doc2Vec as features.

After some tests, I tried using the Flesch-Kincaid index instead of the Flesch index. I also added expanded features, including count of individual words' CEFR levels.

I also tried different methods to integrate the multiple sentences, either has a whole text, as paragraphs, as separate sentences, or as a mean of the separate sentences.

Unfortunately, no significant improvement has been made with those features.

I was also afraid the model was just getting better at copying the Flesch-Kincaid formula.

I then started using the CLEAR corpus instead, that provides a B.T. easiness score for the excerpts.

I also started to use BERT models, particularly bert-base-uncased due to training times becoming very long for certain tests and remaining time for the project was thinning out.

As I tried to find other methods to apply, I found mention of pseudo-labeling in the article of the winner for the CLEAR competition, hosted on Kaggle. I implemented pseudo-labeling by adding evaluation of the 5 closest sentences to all sentences in the base corpus, but as the results were getting a bit better, it wasn't groundbreaking. Unfortunately, I ran out of time as I was trying to optimize it and reduce smartly the number of pseudo-labeled sentences used.

## With more time

With more time, I would have restarted the code from zero. Firstly, because many things aren't used anymore, such as SVM and Doc2Vec, but also because I learned many things along the way that I made harder unintentionally. Better hardware usage(thus, computing performance) could also be expected from such a rework.

I believe finding a bigger dataset with B.T. easiness could also help a lot, or using pseudo-labeling more efficiently if none can be found.
