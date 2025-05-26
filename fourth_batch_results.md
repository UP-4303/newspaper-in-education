# Fourth batch results

This is the full log from the fourth batch, separated by markdown headers.  
If you look carefully, you will notice some models being "loaded" instead of "trained", this is simply because they were already trained and saved.

vecSize takes the values [10, 25, 50, 75, 100, 125, 150, 200]. The default value, setup by the `gensim` package is 100.  
epochs takes the values [1, 5, 7, 10, 12, 15, 20]. The default value, setup by the `gensim` package is 10.

## vecSize 10, epochs 1

Loading doc2vec with vecSize 10, epochs 1  
Training SVM with vecSize 10, epochs 1  
100%|██████████| 397/397 [00:01<00:00, 262.51it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [09:34<00:00, 57.05it/s]  
Correct predictions 10786/32803, 32.88113892022071%  
Error 31273, mean error 0.9533579245800688

## vecSize 10, epochs 5

Loading doc2vec with vecSize 10, epochs 5  
Training SVM with vecSize 10, epochs 5  
100%|██████████| 397/397 [00:02<00:00, 157.87it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [10:59<00:00, 49.75it/s]  
Correct predictions 11470/32803, 34.96631405664116%  
Error 29677, mean error 0.9047038380635918

## vecSize 10, epochs 7

Loading doc2vec with vecSize 10, epochs 7  
Training SVM with vecSize 10, epochs 7  
100%|██████████| 397/397 [00:03<00:00, 118.37it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [11:43<00:00, 46.62it/s]  
Correct predictions 11992/32803, 36.5576319239094%  
Error 28639, mean error 0.873060390817913

## vecSize 10, epochs 10

Training doc2vec with vecSize 10, epochs 10  
Saving...  
Training SVM with vecSize 10, epochs10  
100%|██████████| 397/397 [00:03<00:00, 104.98it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [12:01<00:00, 45.50it/s]  
Correct predictions 12424/32803, 37.87458464164863%  
Error 26925, mean error 0.8208090723409445  

## vecSize 10, epochs 12

Training doc2vec with vecSize 10, epochs 12  
Saving...  
Training SVM with vecSize 10, epochs12  
100%|██████████| 397/397 [00:02<00:00, 147.39it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [12:31<00:00, 43.66it/s]  
Correct predictions 12686/32803, 38.67329207694418%  
Error 26186, mean error 0.7982806450629516  

## vecSize 10, epochs 15

Training doc2vec with vecSize 10, epochs 15  
Saving...  
Training SVM with vecSize 10, epochs15  
100%|██████████| 397/397 [00:05<00:00, 75.18it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [14:01<00:00, 38.97it/s]  
Correct predictions 12812/32803, 39.05740328628479%  
Error 25777, mean error 0.7858122732676889  

## vecSize 10, epochs 20

Training doc2vec with vecSize 10, epochs 20  
Saving...  
Training SVM with vecSize 10, epochs20  
100%|██████████| 397/397 [00:07<00:00, 56.54it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [18:46<00:00, 29.13it/s]  
Correct predictions 12986/32803, 39.587842575374204%  
Error 25383, mean error 0.7738011767216413  

## vecSize 25, epochs 1

Training doc2vec with vecSize 25, epochs 1  
Saving...  
Training SVM with vecSize 25, epochs1  
100%|██████████| 397/397 [00:02<00:00, 167.27it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [18:53<00:00, 28.94it/s]  
Correct predictions 10771/32803, 32.83541139529921%  
Error 31298, mean error 0.9541200499954272  

## vecSize 25, epochs 5

Training doc2vec with vecSize 25, epochs 5  
Saving...  
Training SVM with vecSize 25, epochs5  
100%|██████████| 397/397 [00:01<00:00, 290.25it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [14:57<00:00, 36.55it/s]  
Correct predictions 12009/32803, 36.609456452153765%  
Error 28410, mean error 0.8660793220132305  

## vecSize 25, epochs 7

Training doc2vec with vecSize 25, epochs 7  
Saving...  
Training SVM with vecSize 25, epochs7  
100%|██████████| 397/397 [00:03<00:00, 108.72it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [13:44<00:00, 39.80it/s]  
Correct predictions 12471/32803, 38.017864219736%  
Error 27230, mean error 0.8301070024083164  

## vecSize 25, epochs 10

Training doc2vec with vecSize 25, epochs 10  
Saving...  
Training SVM with vecSize 25, epochs10  
100%|██████████| 397/397 [00:04<00:00, 95.64it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [14:30<00:00, 37.68it/s]  
Correct predictions 12859/32803, 39.20068286437216%  
Error 26104, mean error 0.7957808737005762  

## vecSize 25, epochs 12

Training doc2vec with vecSize 25, epochs 12  
Saving...  
Training SVM with vecSize 25, epochs12  
100%|██████████| 397/397 [00:02<00:00, 160.25it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [15:09<00:00, 36.06it/s]  
Correct predictions 12849/32803, 39.17019784775783%  
Error 25810, mean error 0.786818278815962  

## vecSize 25, epochs 15

Training doc2vec with vecSize 25, epochs 15  
Saving...  
Training SVM with vecSize 25, epochs15  
100%|██████████| 397/397 [00:05<00:00, 70.73it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [18:46<00:00, 29.12it/s]  
Correct predictions 12965/32803, 39.5238240404841%  
Error 25349, mean error 0.772764686156754  

## vecSize 25, epochs 20

Training doc2vec with vecSize 25, epochs 20  
Saving...  
Training SVM with vecSize 25, epochs20  
100%|██████████| 397/397 [00:08<00:00, 49.34it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [20:00<00:00, 27.32it/s]  
Correct predictions 13118/32803, 39.99024479468341%  
Error 25278, mean error 0.7706002499771363  

## vecSize 50, epochs 1

Training doc2vec with vecSize 50, epochs 1  
Saving...  
Training SVM with vecSize 50, epochs1  
100%|██████████| 397/397 [00:01<00:00, 298.66it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [13:18<00:00, 41.08it/s]  
Correct predictions 10752/32803, 32.77748986373197%  
Error 31319, mean error 0.9547602353443283  

## vecSize 50, epochs 5

Training doc2vec with vecSize 50, epochs 5  
Saving...  
Training SVM with vecSize 50, epochs5  
100%|██████████| 397/397 [00:02<00:00, 141.98it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [14:59<00:00, 36.48it/s]  
Correct predictions 12037/32803, 36.6948144986739%  
Error 28341, mean error 0.8639758558668414  

## vecSize 50, epochs 7

Training doc2vec with vecSize 50, epochs 7  
Saving...  
Training SVM with vecSize 50, epochs7  
100%|██████████| 397/397 [00:03<00:00, 103.75it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [20:32<00:00, 26.60it/s]  
Correct predictions 12521/32803, 38.17028930280767%  
Error 26992, mean error 0.8228515684541048  

## vecSize 50, epochs 10

Training doc2vec with vecSize 50, epochs 10  
Saving...  
Training SVM with vecSize 50, epochs10  
100%|██████████| 397/397 [00:04<00:00, 88.20it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [19:59<00:00, 27.35it/s]  
Correct predictions 12794/32803, 39.00253025637899%  
Error 26211, mean error 0.79904277047831  

## vecSize 50, epochs 12

Training doc2vec with vecSize 50, epochs 12  
Saving...  
Training SVM with vecSize 50, epochs12  
100%|██████████| 397/397 [00:04<00:00, 81.56it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [17:38<00:00, 30.99it/s]  
Correct predictions 12856/32803, 39.191537359387866%  
Error 25602, mean error 0.7804773953601805  

## vecSize 50, epochs 15

Training doc2vec with vecSize 50, epochs 15  
Saving...  
Training SVM with vecSize 50, epochs15  
100%|██████████| 397/397 [00:05<00:00, 66.37it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [22:38<00:00, 24.15it/s]  
Correct predictions 12955/32803, 39.493339023869765%  
Error 25481, mean error 0.776788708349846  

## vecSize 50, epochs 20

Training doc2vec with vecSize 50, epochs 20  
Saving...  
Training SVM with vecSize 50, epochs20  
100%|██████████| 397/397 [00:10<00:00, 39.65it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [24:50<00:00, 22.00it/s]  
Correct predictions 13125/32803, 40.011584306313445%  
Error 25370, mean error 0.773404871505655  

## vecSize 75, epochs 1

Training doc2vec with vecSize 75, epochs 1  
Saving...  
Training SVM with vecSize 75, epochs1  
100%|██████████| 397/397 [00:01<00:00, 302.49it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [16:48<00:00, 32.51it/s]  
Correct predictions 10784/32803, 32.87504191689784%  
Error 31237, mean error 0.9522604639819529  

## vecSize 75, epochs 5

Training doc2vec with vecSize 75, epochs 5  
Saving...  
Training SVM with vecSize 75, epochs5  
100%|██████████| 397/397 [00:02<00:00, 183.22it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [18:33<00:00, 29.45it/s]  
Correct predictions 12113/32803, 36.92650062494284%  
Error 28140, mean error 0.8578483675273603  

## vecSize 75, epochs 7

Training doc2vec with vecSize 75, epochs 7  
Saving...  
Training SVM with vecSize 75, epochs7  
100%|██████████| 397/397 [00:03<00:00, 103.37it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [19:48<00:00, 27.59it/s]  
Correct predictions 12582/32803, 38.356247904155104%  
Error 26835, mean error 0.8180654208456544  

## vecSize 75, epochs 10

Training doc2vec with vecSize 75, epochs 10  
Saving...  
Training SVM with vecSize 75, epochs10  
100%|██████████| 397/397 [00:04<00:00, 79.42it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [20:46<00:00, 26.31it/s]  
Correct predictions 12899/32803, 39.322622930829496%  
Error 25689, mean error 0.7831295918056276  

## vecSize 75, epochs 12

Training doc2vec with vecSize 75, epochs 12  
Saving...  
Training SVM with vecSize 75, epochs12  
100%|██████████| 397/397 [00:05<00:00, 70.88it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [21:41<00:00, 25.21it/s]  
Correct predictions 12973/32803, 39.548212053775565%  
Error 25664, mean error 0.7823674663902692  

## vecSize 75, epochs 15

Training doc2vec with vecSize 75, epochs 15  
Saving...  
Training SVM with vecSize 75, epochs15  
100%|██████████| 397/397 [00:06<00:00, 64.09it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [24:04<00:00, 22.72it/s]  
Correct predictions 12999/32803, 39.627473096972835%  
Error 25396, mean error 0.7741974819376276  

## vecSize 75, epochs 20

Training doc2vec with vecSize 75, epochs 20  
Saving...  
Training SVM with vecSize 75, epochs20  
100%|██████████| 397/397 [00:09<00:00, 43.34it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [24:03<00:00, 22.72it/s]  
Correct predictions 13258/32803, 40.417035027284086%  
Error 25005, mean error 0.762277840441423  

## vecSize 100, epochs 1

Training doc2vec with vecSize 100, epochs 1  
Saving...  
Training SVM with vecSize 100, epochs1  
100%|██████████| 397/397 [00:01<00:00, 312.33it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [17:03<00:00, 32.05it/s]  
Correct predictions 10768/32803, 32.82626589031491%  
Error 31240, mean error 0.9523519190317958  

## vecSize 100, epochs 5

Training doc2vec with vecSize 100, epochs 5  
Saving...  
Training SVM with vecSize 100, epochs5  
100%|██████████| 397/397 [00:02<00:00, 150.49it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [18:45<00:00, 29.13it/s]  
Correct predictions 12175/32803, 37.115507727951716%  
Error 27977, mean error 0.8528793098192239  

## vecSize 100, epochs 7

Training doc2vec with vecSize 100, epochs 7  
Saving...  
Training SVM with vecSize 100, epochs7  
100%|██████████| 397/397 [00:03<00:00, 125.60it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [18:44<00:00, 29.18it/s]  
Correct predictions 12549/32803, 38.2556473493278%  
Error 26907, mean error 0.8202603420418864  

## vecSize 100, epochs 10

Loading doc2vec with vecSize 100, epochs 10  
Training SVM with vecSize 100, epochs10  
100%|██████████| 397/397 [00:04<00:00, 88.43it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [19:32<00:00, 27.97it/s]  
Correct predictions 12939/32803, 39.44456299728684%  
Error 25617, mean error 0.7809346706093955  
  
## vecSize 100, epochs 12

Training doc2vec with vecSize 100, epochs 12  
Saving...  
Training SVM with vecSize 100, epochs12  
100%|██████████| 397/397 [00:05<00:00, 75.67it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [21:06<00:00, 25.91it/s]  
Correct predictions 13048/32803, 39.77684967838307%  
Error 25460, mean error 0.7761485230009451  

## vecSize 100, epochs 15

Training doc2vec with vecSize 100, epochs 15  
Saving...  
Training SVM with vecSize 100, epochs15  
100%|██████████| 397/397 [00:06<00:00, 62.37it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [21:03<00:00, 25.95it/s]  
Correct predictions 12946/32803, 39.46590250891687%  
Error 25491, mean error 0.7770935585159894  

## vecSize 100, epochs 20

Training doc2vec with vecSize 100, epochs 20  
Saving...  
Training SVM with vecSize 100, epochs20  
100%|██████████| 397/397 [00:06<00:00, 58.60it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [20:24<00:00, 26.79it/s]  
Correct predictions 13191/32803, 40.21278541596805%  
Error 25413, mean error 0.7747157272200713  

## vecSize 125, epochs 1

Training doc2vec with vecSize 125, epochs 1  
Saving...  
Training SVM with vecSize 125, epochs1  
100%|██████████| 397/397 [00:01<00:00, 332.34it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [16:45<00:00, 32.62it/s]  
Correct predictions 10814/32803, 32.96649696674085%  
Error 31153, mean error 0.9496997225863488  

## vecSize 125, epochs 5

Training doc2vec with vecSize 125, epochs 5  
Saving...  
Training SVM with vecSize 125, epochs5  
100%|██████████| 397/397 [00:02<00:00, 157.72it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [17:56<00:00, 30.48it/s]  
Correct predictions 12238/32803, 37.30756333262202%  
Error 27937, mean error 0.8516599091546505  

## vecSize 125, epochs 7

Training doc2vec with vecSize 125, epochs 7  
Saving...  
Training SVM with vecSize 125, epochs7  
100%|██████████| 397/397 [00:03<00:00, 128.03it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [18:01<00:00, 30.34it/s]  
Correct predictions 12585/32803, 38.36539340913941%  
Error 26947, mean error 0.8214797427064597  

## vecSize 125, epochs 10

Training doc2vec with vecSize 125, epochs 10  
Saving...  
Training SVM with vecSize 125, epochs10  
100%|██████████| 397/397 [00:02<00:00, 173.03it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [19:31<00:00, 28.00it/s]  
Correct predictions 12903/32803, 39.33481693747523%  
Error 25564, mean error 0.7793189647288358  

## vecSize 125, epochs 12

Training doc2vec with vecSize 125, epochs 12  
Saving...  
Training SVM with vecSize 125, epochs12  
100%|██████████| 397/397 [00:03<00:00, 129.42it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [19:47<00:00, 27.62it/s]  
Correct predictions 13062/32803, 39.819528701643144%  
Error 25365, mean error 0.7732524464225833  

## vecSize 125, epochs 15

Training doc2vec with vecSize 125, epochs 15  
Saving...  
Training SVM with vecSize 125, epochs15  
100%|██████████| 397/397 [00:06<00:00, 62.97it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [21:32<00:00, 25.37it/s]  
Correct predictions 13050/32803, 39.782946681705944%  
Error 25400, mean error 0.774319422004085  

## vecSize 125, epochs 20

Training doc2vec with vecSize 125, epochs 20  
Saving...  
Training SVM with vecSize 125, epochs20  
100%|██████████| 397/397 [00:07<00:00, 51.41it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [22:49<00:00, 23.95it/s]  
Correct predictions 13203/32803, 40.249367435905256%  
Error 25086, mean error 0.7647471267871842  

## vecSize 150, epochs 1

Training doc2vec with vecSize 150, epochs 1  
Saving...  
Training SVM with vecSize 150, epochs1  
100%|██████████| 397/397 [00:01<00:00, 365.33it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [22:03<00:00, 24.78it/s]  
Correct predictions 10925/32803, 33.304880651159955%  
Error 30774, mean error 0.9381459012895162  

## vecSize 150, epochs 5

Training doc2vec with vecSize 150, epochs 5  
Saving...  
Training SVM with vecSize 150, epochs5  
100%|██████████| 397/397 [00:02<00:00, 155.04it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [23:16<00:00, 23.48it/s]  
Correct predictions 12091/32803, 36.859433588391305%  
Error 28138, mean error 0.8577873974941317  

## vecSize 150, epochs 7

Training doc2vec with vecSize 150, epochs 7  
Saving...  
Training SVM with vecSize 150, epochs7  
100%|██████████| 397/397 [00:02<00:00, 137.93it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [23:24<00:00, 23.35it/s]  
Correct predictions 12528/32803, 38.191628814437706%  
Error 27109, mean error 0.8264183153979819  

## vecSize 150, epochs 10

Training doc2vec with vecSize 150, epochs 10  
Saving...  
Training SVM with vecSize 150, epochs10  
100%|██████████| 397/397 [00:03<00:00, 102.27it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [24:50<00:00, 22.01it/s]  
Correct predictions 12888/32803, 39.28908941255373%  
Error 25837, mean error 0.7876413742645489  

## vecSize 150, epochs 12

Training doc2vec with vecSize 150, epochs 12  
Saving...  
Training SVM with vecSize 150, epochs12  
100%|██████████| 397/397 [00:04<00:00, 89.03it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [25:39<00:00, 21.31it/s]  
Correct predictions 13004/32803, 39.64271560528%  
Error 25494, mean error 0.7771850135658324  

## vecSize 150, epochs 15

Training doc2vec with vecSize 150, epochs 15  
Saving...  
Training SVM with vecSize 150, epochs15  
100%|██████████| 397/397 [00:05<00:00, 72.26it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [26:56<00:00, 20.29it/s]  
Correct predictions 12944/32803, 39.459805505594%  
Error 25475, mean error 0.7766057982501601  

## vecSize 150, epochs 20

Training doc2vec with vecSize 150, epochs 20  
Saving...  
Training SVM with vecSize 150, epochs20  
100%|██████████| 397/397 [00:07<00:00, 56.30it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [28:15<00:00, 19.35it/s]  
Correct predictions 13203/32803, 40.249367435905256%  
Error 25213, mean error 0.7686187238972045  

## vecSize 200, epochs 1

Training doc2vec with vecSize 200, epochs 1  
Saving...  
Training SVM with vecSize 200, epochs1  
100%|██████████| 397/397 [00:01<00:00, 319.17it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [29:56<00:00, 18.26it/s]  
Correct predictions 10737/32803, 32.731762338810476%  
Error 31409, mean error 0.9575038868396183  

## vecSize 200, epochs 5

Training doc2vec with vecSize 200, epochs 5  
Saving...  
Training SVM with vecSize 200, epochs5  
100%|██████████| 397/397 [00:02<00:00, 151.86it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [28:34<00:00, 19.13it/s]  
Correct predictions 11993/32803, 36.56068042557083%  
Error 28442, mean error 0.8670548425448892  

## vecSize 200, epochs 7

Training doc2vec with vecSize 200, epochs 7  
Saving...  
Training SVM with vecSize 200, epochs7  
100%|██████████| 397/397 [00:03<00:00, 123.19it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [29:11<00:00, 18.72it/s]  
Correct predictions 12513/32803, 38.1459012895162%  
Error 27032, mean error 0.8240709691186782  

## vecSize 200, epochs 10

Training doc2vec with vecSize 200, epochs 10  
Saving...  
Training SVM with vecSize 200, epochs10  
100%|██████████| 397/397 [00:04<00:00, 96.59it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [29:46<00:00, 18.37it/s]  
Correct predictions 12840/32803, 39.14276133280492%  
Error 25891, mean error 0.789287565161723  

## vecSize 200, epochs 12

Training doc2vec with vecSize 200, epochs 12  
Saving...  
Training SVM with vecSize 200, epochs12  
100%|██████████| 397/397 [00:04<00:00, 85.14it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [31:21<00:00, 17.43it/s]  
Correct predictions 12976/32803, 39.55735755875987%  
Error 25748, mean error 0.7849282077858732  

## vecSize 200, epochs 15

Training doc2vec with vecSize 200, epochs 15  
Saving...  
Training SVM with vecSize 200, epochs15  
100%|██████████| 397/397 [00:05<00:00, 67.13it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [33:33<00:00, 16.29it/s]  
Correct predictions 12976/32803, 39.55735755875987%  
Error 25566, mean error 0.7793799347620645  

## vecSize 200, epochs 20

Training doc2vec with vecSize 200, epochs 20  
Saving...  
Training SVM with vecSize 200, epochs20  
100%|██████████| 397/397 [00:07<00:00, 54.67it/s]  
Saving...  
Predicting...  
100%|██████████| 32803/32803 [38:26<00:00, 14.22it/s]  
Correct predictions 13210/32803, 40.27070694753528%  
Error 25127, mean error 0.7659970124683718  
