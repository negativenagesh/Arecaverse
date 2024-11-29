<h1 align='center'>
  🌴 Arecanut Quality Classification 🌴
</h1>

<h4 align='center'>
  Enhancing quality grading of areca nut for Arecanut farmers with Machine learning
</h4>

![areca-nut-6344085](https://github.com/user-attachments/assets/45d34d8e-4ce4-4016-8bdb-deec2ba352ec)

## ⚙️ Setup and Installation
1. Fork this repo by clicking 'fork' in right side above, then follow below steps 

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
  Run the script:
```bash
 ./setup.sh
```
  activate env:
```bash
  source areca/bin/activate
```
5. Install dependencies:
```bash
pip install -r required.txt
```
6. Run the app:
```python
streamlit run app/app.py
```
## Problem Statement

<div align="center">
  
  ![image](https://github.com/user-attachments/assets/a84089b3-549b-4395-9d45-3acb3f683039)
</div>

Areca nut quality sorting is a manual process done by farmers, there are more than 6 categories in quality(1st Chali, 2nd Chali, 3rd Chali, 1st Gotu, 2nd Gotu, Kole etc). For example: where I live people make like more than 200 quintols of arecanut(1 quintol=100kg). To sort 1 quintol of areca nut it takes more than a day for 1 farmer who is strong and fit, imagine a household where a farmer grows more than 200 quintol arecanut and where he alone have to do quality sort, it takes more than 40 days for this process, if you consider my area, these days getting labourers is also a tough work, if we get labourers for morning to evening with food, snacks, drinks they ask minimum 900 Rupees, suppose if we get 1 labourer, he may be faster in sorting, but he cant finish 1 quintol in less than 2 hours or so. If you consider areca nut whole sellers they buy thousands of quintols directly without sorting, so if the arecanut is sorted it gets good price(see below graph) they look for hundreads of labourers to sort this manually which might cost them high. Arecanut peeling machine was introduced in 2008(Credit: Google), it does only peeling with less accuracy and there is no machine for quality sorting which uses AI, so when I was thnking for project idea this problem flashed for me which is seen in each and every household in my area and in entire Karnataka region, so this project is aimed to make arecanut quality sorting without human internvention.

## Arecanut(Betelnut/Supari) prices in Yellapur market, Karwar(Uttar Kannad), Karnataka

<div align="center">
  
  ![image](https://github.com/user-attachments/assets/7bb863a9-1888-47ca-ba26-2fab39201251)
  
  source: https://agriplus.in/price/arecanut-betelnut-supari/karnataka/karwar-uttar-kannad/yellapur
</div>

## Dataset: 

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
