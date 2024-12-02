<h1 align='center'>
  🌴 Arecanut Quality Classification 🌴
</h1>

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/negativenagesh/Arecanut-quality-classification)](https://github.com/negativenagesh/Arecanut-quality-classification/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/negativenagesh/Arecanut-quality-classification)](https://github.com/negativenagesh/Arecanut-quality-classification/network)
[![GitHub issues](https://img.shields.io/github/issues/negativenagesh/Arecanut-quality-classification)](https://github.com/negativenagesh/Arecanut-quality-classification/issues)
[![GitHub license](https://img.shields.io/github/license/negativenagesh/Arecanut-quality-classification)](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/LICENSE)

</div>

<h4 align='center'>
  Enhancing quality grading of areca nut for Arecanut farmers with Machine learning
</h4>

![areca-nut-6344085](https://github.com/user-attachments/assets/45d34d8e-4ce4-4016-8bdb-deec2ba352ec)

## ⚙️ Setup
1. Star and Fork this repo by clicking 'fork' in right side above, then follow below steps 

2. Clone this repo:
```bash
git clone https://github.com/yourusername/arecanut-quality-classification.git
```
3. Create venv or do 4th step:
```bash
py -3.12 -m venv areca

source areca/Scripts/activate
```
4. Run setup.sh
   
   Make the script executable(if it is not already):
```bash
 chmod +x setup.sh
```
  Run the script:(includes all the dependencies, libraries etc..)
```bash
 ./setup.sh
```
  activate env:
```bash
  source areca/bin/activate
```
5. Install dependencies:(if followed step 4 don't run it simply)
```bash
pip install -r required.txt
```
6. API set-up: 
 ```
 Create a new file named .env in the root directory of the project:
 Get your free API keys from here by signing in:
```
[newsapi.org](https://newsapi.org/) | 
[weatherstack.com](https://weatherstack.com/)
```
  Add your API keys to .env in the same manner like below:
```
```env
NEWS_API_KEY= xxxxxxxxxxxxxxxxxxxxxxxxx
WEATHER_API_KEY= xxxxxxxxxxxxxxxxxxxxxxxxx
```

8. Run the app:
```python
streamlit run app/app.py
```
## Frontend:

<div align="center">

  ![Screenshot 2024-12-03 004449](https://github.com/user-attachments/assets/30f13ddd-03e3-43a7-8a5c-254c6db36ceb)
  ![Screenshot 2024-12-03 004502](https://github.com/user-attachments/assets/33a079e9-d3ad-458a-8d25-ed0fcce84df6)


</div>

## Problem Statement

<div align="center">
  
  ![image](https://github.com/user-attachments/assets/a84089b3-549b-4395-9d45-3acb3f683039)
</div>

Areca nut quality sorting is a manual process done by farmers, there are more than 6 categories in quality(1st Chali, 2nd Chali, 3rd Chali, 1st Gotu, 2nd Gotu, Kole etc). For example: where I live people make like more than 200 quintols of arecanut(1 quintol=100kg). To sort 1 quintol of areca nut it takes more than a day for 1 farmer who is strong and fit, imagine a household where a farmer grows more than 200 quintol arecanut and where he alone have to do quality sort, it takes more than 40 days for this process, if you consider my area, these days getting labourers is also a tough work, if we get labourers for morning to evening with food, snacks, drinks they ask minimum 900 Rupees, suppose if we get 1 labourer, he may be faster in sorting, but he cant finish 1 quintol in less than a day or so. If you consider areca nut whole sellers they buy thousands of quintols directly without sorting, so if the arecanut is sorted it gets good price(see below graph) they look for hundreads of labourers to sort this manually which might cost them high. Arecanut peeling machine was introduced in 2008(Credit: Google), it does only peeling with less accuracy and there is no machine for quality sorting which uses AI, so when I was thnking for project idea this problem flashed for me which is seen in each and every household in my area and in entire Karnataka region, so this project is aimed to make arecanut quality sorting without human internvention.

Once the machine learns, it can analyze new arecanuts using cameras or sensors. It quickly decides the quality of each nut and separates them into categories—just like a skilled farmer would, but much faster and more consistently.

## Reducing Human Work

Traditionally, sorting arecanuts is done by people sitting for hours, carefully inspecting each nut. This job is:

* Exhausting: It requires constant focus and attention, which is physically and mentally tiring.
* Time-Consuming: Sorting a large number of arecanuts can take days or even weeks, depending on the quantity.
* Prone to Mistakes: When people work for long hours, they can misjudge the quality of nuts or miss some details.

With a machine:

* The sorting is done automatically. People don’t need to sit and sort for hours.
* Farmers or workers only need to supervise the machine to ensure it’s working correctly.
* The machine works faster and more accurately, reducing the chances of errors.
* This means that the hard part of the job is done by the machine, while people can focus on other tasks or just oversee the process.

## Benefits to Farmers:
1. Saves Time:
For a farmer, time is precious. If they spend days sorting arecanuts, they lose time they could use for other important tasks like taking care of their crops or selling their produce. The machine does the sorting in a fraction of the time, allowing farmers to do more in their day.

2. Improves Accuracy:
A machine doesn’t get tired or distracted. It looks at every nut with the same level of focus, ensuring that only the best-quality nuts are marked as good. This means farmers can confidently sell their produce, knowing buyers will be satisfied with the quality.

3. Increases Productivity:
Imagine a farmer with a large harvest of arecanuts. Sorting them all manually would take weeks, but with a machine, the work can be done in hours or days. This allows farmers to process more nuts and sell them quickly, leading to better earnings.

## Market Size and Growth

The areca nut market size in India is estimated at USD 0.92 billion in 2024, with expectations to reach USD 1.16 billion by 2029, reflecting a compound annual growth rate (CAGR) of 4.73% during this period1.
In 2023, the Indian areca nut market was valued at approximately USD 5.9 billion, marking a decrease of 8% compared to the previous year, which ended a six-year growth trend2. This decline was attributed to various factors including production challenges and fluctuating demand.

The demand for areca nuts is primarily driven by their cultural significance and consumption in traditional practices across India. They are commonly used in conjunction with betel leaves and are available in multiple forms such as fresh, dried, roasted, and cured14. Areca nuts play a crucial role in products like gutka and pan masala, which are popular across various demographics in India. The increasing consumption of these products is expected to bolster the market further. 

The India pan masala market was valued at approximately INR 4,23,095 crore (USD 5.28 billion) in 2023 and is projected to grow at a CAGR of around 4.4%, reaching INR 6,23,619 crore (USD 8.28 billion) by 2032123. This growth is driven by changing consumer preferences, with many shifting from traditional tobacco products to pan masala for a perceived healthier alternative.

India remains the largest producer and consumer of areca nuts globally, accounting for about 67.99% of global production as of 20223. The production volume was approximately 1.67 billion kg in 2022, with a notable increase from previous years3. In terms of exports, India exported around 13.37 million kg of areca nuts in 2023, while imports were significantly higher at approximately 39.03 million kg, indicating India's strong consumption needs despite being a major producer.

## Arecanut(Betelnut/Supari) prices in Yellapur market, Karwar(Uttar Kannad), Karnataka

<div align="center">
  
  ![image](https://github.com/user-attachments/assets/7bb863a9-1888-47ca-ba26-2fab39201251)
  
  source: https://agriplus.in/price/arecanut-betelnut-supari/karnataka/karwar-uttar-kannad/yellapur
</div>

## Data collection and preprocessing: 

I didn't find dataset of arecanut images anywhere, so I took pictures of 3 qualities(1, 2, 3) of arecanut images from Nothing phone 2a and here you can find the link to download the images: [kaggle](https://www.kaggle.com/datasets/subrahmanya090/arecanut) 

#### Sample images:

<div align="center" style="display: flex; justify-content: center; align-items: center;">
  <img src="https://github.com/user-attachments/assets/18195188-d94c-46e6-ab94-24997d598109" alt="Image 1" width="200">
  <img src="https://github.com/user-attachments/assets/42472d13-a1e1-4f04-9129-676884ef478d" alt="Image 1" width="200">
  <img src="https://github.com/user-attachments/assets/1ad17f1c-7765-47f2-b0da-89f35342de44" alt="Image 1" width="200">
</div>

## Image preprocessing:

1. Image background removal from - [Rembg](https://github.com/danielgatis/rembg)
   
<div align="center" style="display: flex; justify-content: center; align-items: center;">
  <img src="https://github.com/user-attachments/assets/dffbe152-d99a-4ff2-b5a7-2975b6ece0fc" alt="Image 1" >
  <img src="https://github.com/user-attachments/assets/debada5f-a0c4-4ae4-a1a8-aaaeab5a8d3e" alt="Image 2" width="200">
  <img src="https://github.com/user-attachments/assets/ee8bed3d-bc90-4d9e-b6d7-905318084191" alt="Image 3" width="200">
  <img src="https://github.com/user-attachments/assets/e6e07296-2b03-419d-b76e-53263da302d9" alt="Image 4" width="200">
</div>

2. Resizing (128 * 128)
3. Grayscale convertion
4. GaussianBlur
5. [CLAHE convertion:](https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html)
6. [Sharpening image:](https://medium.com/@sajjadhadi/mastering-opencv2-in-15-days-day-3-image-filtering-and-enhancement-ae1095f09aa5)
7. Canny edge detector:
https://github.com/cynicphoenix/Canny-Edge-Detector
https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
8. Normalizing image

## Final image after preprocessing:

<div align="center" style="display: flex; justify-content: center; align-items: center;">
  <img src="https://github.com/user-attachments/assets/32f82095-8882-4584-a36b-af3ee7ffaa0c" alt="Image 2" width="200">
  <img src="https://github.com/user-attachments/assets/d86ecc22-cf83-44eb-9ac5-8e005fd6d2b5" alt="Image 3" width="200">
  <img src="https://github.com/user-attachments/assets/da59b50d-b5e9-4bb4-86ea-67bc985e82ef" alt="Image 4" width="200">
</div>

Then converted preprocessed images to dataframe each seperately. [Code](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/img-to-df/df.py), then in [EDA.ipynb](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/eda.ipynb), removed unnecessary columns like - "image_name", "file_name", and added column "grade" in all hte datasets seperately WRT quality 1,2,3. Combined all 3 datasets, then shuffled the entire datasets. So at this time I had 4 total datasets, 

1. **Original dataset with shape** - (1582, 16385), with quality 1,2,3 as (559, 16386), (495, 16386), (528, 16386) respectively,
2. Used **SMOTE** to oversample quality 2 and 3 to make equal to quality 1 [arecanut.csv](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/arecanut-SMOTE.csv),
3. Original dataset and smoted dataset didnt perform well, when tested qulaity 3 was not recognized so oversampled only grade 3, [arecanut-SMOTE-oversampled-grade3.csv](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/arecanut-SMOTE-oversampled-grade3.csv),
4. When oversampled last dataset that also didnt perform well but grade 2 was always correctly classified, so oversampled grade 1 and 3 except 2[arecanut-SMOTE-oversampled-grade1&3](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/arecanut-SMOTE-oversampled-grade1%263%3D1000.csv).
5. Did train-test split with test_size=0.2.

## Model selection, justification, Training, Evaluation, Insights, Limitations, Improvements:

In [EDA.ipynb](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/eda.ipynb), as this dataset involves multiclass classification(grade - 1,2,3), the first model which comes to mind is DecisionTreeClassifier which is very robust for any type of datsets when it comes to classification. 

### 1. DecisionTreeClassifier(random_state=42, min_samples_split=10, min_samples_leaf=1):[LINK](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/eda.ipynb)

  * Here, before training this model, I have splitted the original dataset, then scaled it, then trained it and got accuracy of 0.64 which is very bad.

### 2. Left above model and started doing Ensemble model:[LINK](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/eda.ipynb) 

  * created a function "create_bagged_data(df, n_bags=5)" which takes dataset and creates 5 bags with random sample, but here i had given random_state=42, when I further went ahead, I realized by giving random_state=42, it created 5 bags, but as random_state was 42 in each bag it was random data but all bags had same data. Then in this function each bag had train_test_split with test_size=0.2. Then further with these model - DecisionTreeClassifier(random_state=42, min_samples_split=10, min_samples_leaf=1) all bags were trained and tested and with cross_val_score, as each bag had same data, got the cross_val_score = 0.77 for all 5 bag, and test accuracy as 0.86 which is pretty good. In this same link itself you can find confusion matrix as well. and created pickle file of this model (modeldtree)[https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/models/modeldtree], and saved to app.py, and when pressed "check quality" button this model runs in backend. So when I gave both grade 1 and 3 it only classified as 2 so left this model and started creating new one.

### 3. Different hyperparameter testing of DecisionTreeClassifier now onwards:

  * Now also used create_bagged_data(df, n_bags=10, sample_size=1500) function, but now used 10 bags, with random sample = 1500 not as above, all bags now have random data from original dataset, rest all same as above. changed parameter of DecisionTreeClassifier(random_state=42, min_samples_split=10, min_samples_leaf=1) to DecisionTreeClassifier(random_state=42, min_samples_split=10, min_samples_leaf=1,max_depth=50), in last model I haven't used hyperparameter max_depth, here I have assigned it to 50 means depth of the tree will be 50 meaning it will be splitted 50 times got - Bag 1 - Test Accuracy: 0.81,Bag 2 - Test Accuracy: 0.79, Bag 3 - Test Accuracy: 0.81, Bag 4 - Test Accuracy: 0.80, Bag 5 - Test Accuracy: 0.78, Bag 6 - Test, Accuracy: 0.72, Bag 7 - Test Accuracy: 0.79, Bag 8 - Test Accuracy: 0.78, Bag 9 - Test Accuracy: 0.78, Bag 10 - Test Accuracy: 0.88. Bag 10 (bag[9]) had 0.88 accuracy, so I choosed bag 10, and trained decisiontree, and saved it in "baggging+dtree" .pkl file. But in frontend, when I gave an image, it also performed very badly. It only classified grade correctly and some grade 1 arecanuts.

### 4. Applied SMOTE and Trained (equilibrium, oversampling grade 1and grade 3):

  * Used same create_bagged_data(df, n_bags=10, sample_size=1800) function with data2 which is oversampled grade 3 to 750 samples, higher than other 2 grades, I used this because, grade when I gave images except 2nd grade all were classified as grade 1, so I oversampled grade 3 to train it more accurately. But as of now I believed Decision trees would give more accuracy, so i sticked with this model, so same as above I used create_bagged_data(df, n_bags=10, sample_size=1800), as the dataset become large random samples of 1800 rows was taken, and created 10 bags with each random 1800 rows from "data2", and as I told above here onwards i used same models with different hyperparameters, here used **DecisionTreeClassifier(random_state=42, min_samples_split=10, min_samples_leaf=1,max_depth=50),** and got accuracy of 0.86 for bag[6],
  
  * **now changed parameters** - **DecisionTreeClassifier(criterion='entropy',random_state=42, min_samples_split=10, min_samples_leaf=1,max_depth=40)**, here used **entropy** instead of default gini impurity, which helped in growing accuracy, and also changed max_depth to 40, and got highest accuracy for bag[6] 0.86,
  
  * **changed parameters**: **DecisionTreeClassifier(criterion='entropy',random_state=42, min_samples_split=5, min_samples_leaf=1,max_depth=40)**, changed min_samples_split = 5, which is number of samples requires to split a node, got accuracy 0.87 for bag[6], 0.1 increase with compared to last model.

### 5. Voting Classifier: [EDA.ipynb](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/eda.ipynb)

* **Used base model as same as above but with different hyperparameters**: **DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=6, min_samples_leaf=1, max_depth=40)** with 10 of these same models, also used same 10 bags with same econsequences as mentioned above, and each bag is trained with each respective model, meaning bag[0] --> clf[0]..., and also used weights - for each bag base weights were - 3, as im using same data from above which is data2 with same model and different hyperparameters, as I know the accuracies, i have given weight 3 to some bags, weight of bag[6]=9 (highest weight=9) because bag[6] gave highest accuracy 0.87, weight of bag[7] = 1, which has least accuracy in last step, so when I trained **VotingClassifier(estimators=clfs, voting='hard', weights=weights, n_jobs=-1)** got highest individual accuracy for bag[6]=0.88, finally voting classifier gave 0.86 as accuracy, so I made a .pkl file named [bagging+dtree+voting](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/models/bagging%2Bdtree%2Bvoting), but when used in frontend to test, this model also was predicting as grade 1, except grade 2 arecanut.

* **changed hyperparameters and data with data1(oversampling of grade 3)**: as same **create_bagged_data(df, n_bags=10, sample_size=1600)** used with data1 now, with random sample in each bag with 1600 samples, used estimator for voting classifier as **DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=6, min_samples_leaf=1, max_depth=40)**, with voting classifier as **VotingClassifier(estimators=clfs, voting='hard', weights=weights, n_jobs=-1)**, as usual trained with data1(oversampled grade 3, remaining same as original) and got highest accuracy for bag[0] = 0.84 and bag[5] = 0.84, and voting classifier also gave 0.84 accuracy, confusion matrix also can be found in this nmotebook. Created pickle file named [bagging+dtree+voting+data1](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/models/bagging%2Bdtree%2Bvoting%2Bdata1), and this model also performed similar to above model of voting classifier,

* **changed data with data(original data for voting classifier)**: as same used **create_bagged_data(df, n_bags=10, sample_size=1582)**, **DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=6, min_samples_leaf=1, max_depth=40)**, **VotingClassifier(estimators=clfs, voting='hard', weights=weights, n_jobs=-1)**, with changed weights, base weight = 3, weights[6]=9, weights[7]=1, got highest accuracy for bag[8] and bag[9] of 0.85, and voting classifier gave 0.83. Created pickle file of this model named - [bagging+dtree+voting+dataoriginal](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/models/bagging%2Bdtree%2Bvoting%2Bdataoriginal), this model also did not performed well in frontend.

* **changed data with data2(data2 - oversampled grade 3, for voting classifier)**: **create_bagged_data(df, n_bags=10, sample_size=1700)**, **DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=6, min_samples_leaf=1, max_depth=40)**, **VotingClassifier(estimators=clfs, voting='hard', weights=weights, n_jobs=-1)**, with changed weights because ran tis model without giving weights, base weight = 3, weights[9]=9, weights[5]=6, weights[7]=6, got highest accuracy for bag[9] with 0.87, but voting classifier gave 0.83 accuracy, created a pickle file named [bagging+dtree+voting+data2](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/models/bagging%2Bdtree%2Bvoting%2Bdata2), this model also did not performed well in the fronted when tested,

* **changed hyperparameter data with data3(data3 - oversampled grade 3 as well as grade 1 equally, for voting classifier)**: as the grade 2 was classified correctly each time, didn't oversampled it simply, used **create_bagged_data(df, n_bags=10, sample_size=2400)**, **DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=6, min_samples_leaf=1, max_depth=40)**, **VotingClassifier(estimators=clfs, voting='hard', weights=weights, n_jobs=-1)**, with base weight = 3, and weights=[3], weights[1]=9, weights[9]=9, weights[1]=6. Got highest accuracies for some bags of 0.85, but voting classifier gave 0.84 as accuracy,

*  **same data - data3 with different hyperparameter**: used **create_bagged_data(df, n_bags=10, sample_size=2400)**, **DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=6, min_samples_leaf=1, max_depth=40)**, **VotingClassifier(estimators=clfs, voting='hard', weights=weights, n_jobs=-1)** with base weight = 6, weights[9]=9, weights[6]=9. Got highest accuracies for some bags, with accuracy 0.88, voting classifier gave 0.87 as accuracy, so accuracy was good, so made a pickle file named [bagging+dtree+voting+data3](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/models/bagging%2Bdtree%2Bvoting%2Bdata3), as usual this also did not perform well when tested in frontend, except for grade 2,

*  After so many hyperparameter testings, changing models, over sampling, bagging, understood that these models - **DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=6, min_samples_leaf=1)**, **VotingClassifier(estimators=clfs, voting='hard', weights=weights, n_jobs=-1)** would work better with right hyperparameters, so this time removed **max_depth** hyperparameter(by removing this model might have became overfit), and trained with data3, with base weight = 6, weights[9]=9, weights[6]=9, and got highest accuracy ever of **0.89** for **bag[4]**, but voting classifier gave 0.86 accuracy, so now got to know bag[4] of data3 from this above cell would give better accuracy.

* **Finally** using bag[4] from previous step, trained this model - **DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=6, min_samples_leaf=1)**, without any voting classifier or anything, got **accuracy of 0.89**. satisfied with accuracy, and created pickle file named [**bagging+dtree+voting+data3(bag5)**](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/models/bagging%2Bdtree%2Bvoting%2Bdata3(bag5)), and when tested in frontend, I gave images of grade 2 first, predicted most of it with good accuracy, and also gave images of grade 1, for this also predicted most of it with good accuracy, but when tested with grade 3, predicted very badly, for grade 3 it predicted it as grade 1 most of the time.

<div align="center">
  
![image](https://github.com/user-attachments/assets/5251e0d4-92a4-4190-bd75-2d0550e30b4b)
</div>

After careful researching, understood that, when I preprocessed images with many steps I should have stopped at CLAHE convertion, but what wrong I did was converting it after to sharpened image, then again canny edge detection from [here](https://github.com/cynicphoenix/Canny-Edge-Detector), these 2 steps made the features of areca nut very bad. Because consider grade 2 which has white layer on top of it, this made the color mostly white. So even after all these steps of preprocessing this was classified correctly, But considering grade 1 which is cleaner with no layer, mostly brown and dark brown in color, and consider grade 3 which is also similar color of grade 1 with black, dark black, grey etc... but after doing all preprocessing, these 2 arecanuts became almost same in color but not in case of 2nd grade arecanut where this grade was classified correctly, but grade 1 was also classified correctly, only grade 3 was the problem, so i'm doing the preprocessing again after some days.  

## 🎯 Key Objective
Identifying three qualities of areca nuts.

## 🛠️ License 
[Apache License 2.0](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/LICENSE)

## References
1. Image Processing in OpenCV
   https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html

2. The Complete Guide to Image Preprocessing Techniques in Python
   https://medium.com/@maahip1304/the-complete-guide-to-image-preprocessing-techniques-in-python-dca30804550c

3. Basic Operations on Images
   https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html

4. CLAHE (Contrast Limited Adaptive Histogram Equalization)
   https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html

5. Sharpening image in OpenCV
   https://medium.com/@sajjadhadi/mastering-opencv2-in-15-days-day-3-image-filtering-and-enhancement-ae1095f09aa5

6. Areca Nuts - Market Share Analysis, Industry Trends & Statistics, Growth Forecasts (2024 - 2029)
   https://www.giiresearch.com/report/moi1440108-areca-nuts-market-share-analysis-industry-trends.html

7. India - Areca Nuts - Market Analysis, Forecast, Size, Trends and Insights
   https://www.indexbox.io/store/india-areca-nuts-market-report-analysis-and-forecast-to-2020/

8. Perplexity
   https://www.perplexity.ai/search/take-source-from-internet-and-u8Yt5A1qTmKcag1nGY9K3g
