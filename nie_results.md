# NIE Results

This details the different prediction tests made in order to find the most suitable models and parameters for the classification.

## Doc2Vec - SVM

### Flesch - 10 classes

#### First batch - 2k~3k lines datasets

The goal in this first batch was to identify the differences in results if the training dataset of the vectorizer and the one of the classifier weren't of the same size.

As we will see, having the classifier dataset bigger than the vectorizer dataset really worsen the results, while having it smaller gives the best results.  
Increasing the size of both gives slightly better results.

##### Vector size 100, 10 epochs, ~2k lines Doc2vec, ~2k lines SVM

100%|██████████| 33272/33272 [06:12<00:00, 89.22it/s]  
Correct predictions 10902/33272, 32.76628997355133%  
Error 31588, mean error 0.9493868718441933

##### Vector size 100, 10 epochs, ~2k lines Doc2vec, ~3k lines SVM

100%|██████████| 33241/33241 [12:48<00:00, 43.23it/s]  
Correct predictions 7470/33241, 22.472248127312653%  
Error 39912, mean error 1.2006858999428416

##### Vector size 100, 10 epochs, ~3k lines Doc2vec, ~3k lines SVM

100%|██████████| 33241/33241 [12:44<00:00, 43.50it/s]  
Correct predictions 10911/33241, 32.82392226467314%  
Error 30540, mean error 0.918744923437923

##### Vector size 100, 10 epochs, ~3k lines Doc2vec, ~2k lines SVM

100%|██████████| 33241/33241 [12:01<00:00, 46.10it/s]  
Correct predictions 11384/33241, 34.24686381276135%  
Error 30346, mean error 0.9129087572576036

#### Second batch - 10k~20k lines datasets

For this second batch, the goal was to find the best ratio between the size of the training datasets.

As we will see, this would be around `classifier dataset = 3/4 of the vectorizer dataset`, expecting it to scale linearly.

##### Vector size 100, 10 epochs, ~10k lines Doc2vec, ~10k lines SVM

100%|██████████| 33072/33072 [27:33<00:00, 20.00it/s]  
Correct predictions 12069/33072, 36.493105950653124%
Error 28897, mean error 0.8737602805999033

##### Vector size 100, 10 epochs, ~20k lines Doc2vec, ~5k lines SVM

100%|██████████| 32803/32803 [08:55<00:00, 61.26it/s]  
Correct predictions 12336/32803, 37.606316495442485%  
Error 27001, mean error 0.8231259336036338

##### Vector size 100, 10 epochs, ~20k lines Doc2vec, ~7.5k lines SVM

100%|██████████| 32803/32803 [10:46<00:00, 50.70it/s]  
Correct predictions 12413/32803, 37.84105112337286%  
Error 26825, mean error 0.817760570679511

##### Vector size 100, 10 epochs, ~20k lines Doc2vec, ~9k lines SVM

100%|██████████| 32803/32803 [11:58<00:00, 45.64it/s]  
Correct predictions 12474/32803, 38.0270097247203%  
Error 26924, mean error 0.8207785873243301

##### Vector size 100, 10 epochs, ~20k lines Doc2vec, ~10k lines SVM

100%|██████████| 32803/32803 [18:44<00:00, 29.18it/s]  
Correct predictions 12543/32803, 38.23735633935921%  
Error 26626, mean error 0.8116940523732585

##### Vector size 100, 10 epochs, ~20k lines Doc2vec, ~15k lines SVM

100%|██████████| 32803/32803 [19:24<00:00, 28.17it/s]  
Correct predictions 13093/32803, 39.91403225314758%  
Error 25324, mean error 0.7720025607413956

##### Vector size 100, 10 epochs, ~20k lines Doc2vec, ~17.5k lines SVM

100%|██████████| 32803/32803 [26:07<00:00, 20.92it/s]  
Correct predictions 12882/32803, 39.27079840258513%  
Error 25831, mean error 0.787458464164863

##### Vector size 100, 10 epochs, ~20k lines Doc2vec, ~12.5k lines SVM

100%|██████████| 32803/32803 [20:31<00:00, 26.63it/s]  
Correct predictions 12461/32803, 37.98737920312167%  
Error 26747, mean error 0.815382739383593

#### Third batch - 200k~500k lines datasets

For this batch, the goal was to find out if increasing the datasets sizes drastically would also improve the results, and testing the 3/4 ratio at another scale.

This test was stopped due to time constraints and results not being better (even worse than the 20k 15k).

##### Vector size 100, 10 epochs, ~500k lines Doc2vec, ~250k lines SVM

100%|██████████| 18454/18454 [3:35:51<00:00,  1.42it/s]  
Correct predictions 6926/18454, 37.53115855641053%  
Error 15017, mean error 0.813753115855641

##### Vector size 100, 10 epochs, ~500k lines Doc2vec, ~375k lines SVM

100%|██████████| 33328/33328 [7:41:29<00:00,  1.20it/s]  
Correct predictions 13260/33328, 39.78636581853097%  
Error 25832, mean error 0.7750840134421507

#### Fourth batch - 10~200 vector size and 1~20 epochs

For this batch, the goal was to identify improvements by tweaking the vector size and the number of epochs.

Due to the high number of tests (56) only the mean error class error will be included here. The full data will be included unparsed in `fourth_batch_results.md`

| epochs \ vecSize | 10                 | 25                 | 50                 | 75                 | 100                | 125                | 150                | 200                |
|------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| 1                | 0.9533579245800688 | 0.9541200499954272 | 0.9547602353443283 | 0.9522604639819529 | 0.9523519190317958 | 0.9496997225863488 | 0.9381459012895162 | 0.9575038868396183 |
| 5                | 0.9047038380635918 | 0.8660793220132305 | 0.8639758558668414 | 0.8578483675273603 | 0.8528793098192239 | 0.8516599091546505 | 0.8577873974941317 | 0.8670548425448892 |
| 7                | 0.873060390817913  | 0.8301070024083164 | 0.8228515684541048 | 0.8180654208456544 | 0.8202603420418864 | 0.8214797427064597 | 0.8264183153979819 | 0.8240709691186782 |
| 10               | 0.8208090723409445 | 0.7957808737005762 | 0.79904277047831   | 0.7831295918056276 | 0.7809346706093955 | 0.7793189647288358 | 0.7876413742645489 | 0.789287565161723  |
| 12               | 0.7982806450629516 | 0.786818278815962  | 0.7804773953601805 | 0.7823674663902692 | 0.7761485230009451 | 0.7732524464225833 | 0.7771850135658324 | 0.7849282077858732 |
| 15               | 0.7858122732676889 | 0.772764686156754  | 0.776788708349846  | 0.7741974819376276 | 0.7770935585159894 | 0.774319422004085  | 0.7766057982501601 | 0.7793799347620645 |
| 20               | 0.7738011767216413 | 0.7706002499771363 | 0.773404871505655  | 0.762277840441423  | 0.7747157272200713 | 0.7647471267871842 | 0.7686187238972045 | 0.7659970124683718 |

As we can see, having few epochs really hinders the predictions.  
Having many epochs does help getting better results, but not consistently.  
For the vector size, increasing it yields generally better results, but not consistently either.

The 200 vecSize and 20 epochs will now be our reference for testing other models.

## BERT

We will now use regression on the B.T. Easiness value, from the CLEAR corpus.

100%|██████████| 1701/1701 [00:36<00:00, 46.36it/s]  
Error 923.4416349810003, mean error 0.5428816196243388  
Root Mean Square Error 0.6822279044275928

### Tweaks and weight

Changes were made to use the standard error as weight and learning rate tweaking.

100%|██████████| 1701/1701 [00:21<00:00, 79.93it/s]
Error 923.0625320810008, mean error 0.542658749018813
Root Mean Square Error 0.6789603336937857

### Pseudo-labeling

This was achieved by pseudo-labeling the 5 closest sentences (from `external.csv`) to every sentence in the original corpus.

100%|██████████| 1701/1701 [00:22<00:00, 76.89it/s]
Error 858.7093837890005, mean error 0.5048262103403883
Root Mean Square Error 0.6368434036818288

### Other try with pseudo-labeling

I tried reducing the number of pseudo-labeled content, and this was the second best, achieved with 3 pseudo-labeled sentences per sentences of the original corpus.

100%|██████████| 1700/1700 [00:16<00:00, 101.65it/s]
Error 910.1103845250012, mean error 0.535359049720589
Root Mean Square Error 0.6717810088137365
