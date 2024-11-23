import os
import cv2
import numpy as np
from rembg import remove


# Define a consistent output folder
OUTPUT_FOLDER = os.path.abspath("app/output")


def remove_background(input_image_path, temp_output_path):
    """
    Removes the background from an image using `rembg`.
    """
    with open(input_image_path, "rb") as img_file:
        input_data = img_file.read()

    output_data = remove(input_data)

    with open(temp_output_path, "wb") as out_file:
        out_file.write(output_data)


def preprocess_images(input_image_path):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Process a single input image file
    if input_image_path.endswith(('.jpg', '.jpeg', '.png')):
        img = cv2.imread(input_image_path)

        if img is None:
            print(f"Skipping {input_image_path}, unable to read the file.")
            return

        resized_img = cv2.resize(img, (128, 128))
        gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
        blurred_img = cv2.GaussianBlur(gray_img, (5, 5), sigmaX=1.0, sigmaY=1.0)

        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahe_img = clahe.apply(gray_img)

        sharpening_kernel = np.array([[-1, -1, -1],
                                      [-1, 9, -1],
                                      [-1, -1, -1]])
        sharpened_image = cv2.filter2D(clahe_img, -1, sharpening_kernel)

        sobelx = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in X direction
        sobely = cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in Y direction

        gradient_magnitude = np.hypot(sobelx, sobely)
        gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))

        normalized_img = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
        normalized_img = np.uint8(normalized_img)

        output_file_path = os.path.join(OUTPUT_FOLDER, "processed_image.png")
        print("Saving to:", output_file_path)
        cv2.imwrite(output_file_path, normalized_img)
    print("Preprocessing complete. Image saved to:", OUTPUT_FOLDER)


def process_arecanut_image(input_image_path):
    """
    Combines background removal and preprocessing steps.
    """
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    temp_path = os.path.join(OUTPUT_FOLDER, "temp_image.png")
    output_path = os.path.join(OUTPUT_FOLDER, "processed_image.png")

    # Background removal
    remove_background(input_image_path, temp_path)
    if not os.path.exists(temp_path):
        raise RuntimeError(f"Temporary file not created: {temp_path}")

    # Preprocessing
    preprocess_images(temp_path)

    if not os.path.exists(output_path):
        raise RuntimeError(f"Processed file not created: {output_path}")

    return output_path