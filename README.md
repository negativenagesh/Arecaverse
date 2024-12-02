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

## ⚙️ Setup and Installation
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

India remains the largest producer and consumer of areca nuts globally, accounting for about 67.99% of global production as of 20223. The production volume was approximately 1.67 billion kg in 2022, with a notable increase from previous years3. In terms of exports, India exported around 13.37 million kg of areca nuts in 2023, while imports were significantly higher at approximately 39.03 million kg, indicating India's strong consumption needs despite being a major producer

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

1. Original dataset with shape - (1582, 16385), with quality 1,2,3 as (559, 16386), (495, 16386), (528, 16386) respectively,
2. Used SMOTE to oversample quality 2 and 3 to make equal to quality 1 [arecanut.csv](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/arecanut-SMOTE.csv),
3. Original dataset and smoted dataset didnt perform well, when tested qulaity 3 was not recognized so oversampled only grade 3, [arecanut-SMOTE-oversampled-grade3.csv](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/arecanut-SMOTE-oversampled-grade3.csv),
4. When oversampled last dataset that also didnt perform well but grade 2 was always correctly classified, so oversampled grade 1 and 3 except 2[arecanut-SMOTE-oversampled-grade1&3](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/arecanut-SMOTE-oversampled-grade1%263%3D1000.csv).
5. did train-test split with test_size=0.2.

## Model selection and justification:

In [EDA.ipynb](https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/EDA/eda.ipynb), as this dataset involves multiclass classification(grade - 1,2,3), the first model which comes to mind is DecisionTreeClassifier which is very robust for any type of datsets when it comes to classification which ,



## 🎯 Key Objectives
Image Classification: Identify three quality levels of areca nuts.

## Contributors

[Subrahmanya Gaonkar](https://github.com/negativenagesh)

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
