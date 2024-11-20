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


def preprocess_image(input_image_path, output_image_path):
    """
    Preprocesses the image by resizing, converting to grayscale, applying CLAHE,
    sharpening, and calculating Sobel gradients.
    """
    img = cv2.imread(input_image_path)
    if img is None:
        raise ValueError("Unable to read the image after background removal.")

    resized_img = cv2.resize(img, (2048, 2048))
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), sigmaX=1.0, sigmaY=1.0)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(gray_img)

    sharpening_kernel = np.array([[-1, -1, -1],
                                   [-1, 9, -1],
                                   [-1, -1, -1]])
    sharpened_image = cv2.filter2D(clahe_img, -1, sharpening_kernel)

    sobelx = cv2.Sobel(sharpened_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(sharpened_image, cv2.CV_64F, 0, 1, ksize=3)

    gradient_magnitude = np.hypot(sobelx, sobely)
    gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))

    normalized_img = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    normalized_img = np.uint8(normalized_img)

    cv2.imwrite(output_image_path, normalized_img)


def process_arecanut_image(input_image_path, output_folder):
    """
    Combines background removal and preprocessing steps.
    """
    os.makedirs(output_folder, exist_ok=True)
    temp_path = os.path.join(output_folder, "temp_image.png")
    output_path = os.path.join(output_folder, "processed_image.png")

    remove_background(input_image_path, temp_path)
    preprocess_image(temp_path, output_path)

    return output_path