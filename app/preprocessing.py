import os
import cv2
import numpy as np
from rembg import remove


def remove_background(input_image_path, temp_output_path):
    """
    Removes the background from an image using `rembg`.
    """
    with open(input_image_path, "rb") as img_file:
        input_data = img_file.read()

    output_data = remove(input_data)

    with open(temp_output_path, "wb") as out_file:
        out_file.write(output_data)


def preprocess_images(input_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            img = cv2.imread(input_path)

            if img is None:
                print(f"Skipping {filename}, unable to read the file.")
                continue

            resized_img = cv2.resize(img, (128, 128))

            gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
            blurred_img = cv2.GaussianBlur(gray_img, (5, 5), sigmaX=1.0, sigmaY=1.0)
            
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            clahe_img = clahe.apply(gray_img)

                                                                            # blurred_img = cv2.GaussianBlur(gray_img, (9, 9), 0)

                                                                            # source for sharpening images: https://medium.com/@sajjadhadi/mastering-opencv2-in-15-days-day-3-image-filtering-and-enhancement-ae1095f09aa5

            sharpening_kernel = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])
            sharpened_image = cv2.filter2D(clahe_img, -1, sharpening_kernel)
            
            sobelx = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in X direction
            sobely = cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in Y direction
            
            gradient_magnitude = np.hypot(sobelx, sobely)
            gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))
            

                                                                            # source for CLAHE (Contrast Limited Adaptive Histogram Equalization): https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html

            normalized_img = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
            normalized_img = np.uint8(normalized_img)


            cv2.imwrite(output_path, normalized_img)

    print("Preprocessing complete. Images saved to:", output_folder)


def process_arecanut_image(input_image_path, output_folder):
    """
    Combines background removal and preprocessing steps.
    """
    os.makedirs(output_folder, exist_ok=True)
    temp_path = os.path.join(output_folder, "temp_image.png")
    output_path = os.path.join(output_folder, "processed_image.png")

    remove_background(input_image_path, temp_path)
    preprocess_images(temp_path, output_path)

    return output_path