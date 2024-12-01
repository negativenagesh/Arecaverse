import cv2
import numpy as np
from rembg import remove
import os
import csv

def remove_background_in_memory(input_image):
    """
    Removes the background from an image using `rembg`.
    """
    _, buffer = cv2.imencode(".png", input_image)
    output_data = remove(buffer.tobytes())
    bg_removed_image = cv2.imdecode(np.frombuffer(output_data, np.uint8), cv2.IMREAD_UNCHANGED)
    return bg_removed_image

def process_arecanut_image_steps(input_image_path):
    """
    Processes the arecanut image step by step and returns the final preprocessed result.
    """
    # Read input image
    img = cv2.imread(input_image_path)
    if img is None:
        raise ValueError(f"Unable to read the input image: {input_image_path}")

    # Step 1: Remove Background
    bg_removed_img = remove_background_in_memory(img)

    # Step 2: Resize to 256x256
    resized_img = cv2.resize(bg_removed_img, (256, 256))

    # Step 3: Convert to Grayscale
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Step 4: Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(gray_img)

    # Step 5: Apply Sharpening
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened_image = cv2.filter2D(clahe_img, -1, sharpening_kernel)

    # Step 6: Compute Sobel Gradient Magnitude
    sobelx = cv2.Sobel(sharpened_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(sharpened_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.hypot(sobelx, sobely)
    gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))

    return gradient_magnitude

def preprocess_folder(input_folder, output_csv_path):
    """
    Processes all images in a folder and saves the processed arrays to a CSV file.
    """
    # List all image files in the folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        raise ValueError(f"No images found in the folder: {input_folder}")

    # Open the CSV file for writing
    with open(output_csv_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Image_Name"] + [f"Pixel_{i}" for i in range(256 * 256)])  # Updated for 256x256

        for image_file in image_files:
            image_path = os.path.join(input_folder, image_file)
            try:
                # Process the image and convert to a flattened array
                processed_image = process_arecanut_image_steps(image_path)
                resized_image = cv2.resize(processed_image, (256, 256))  # Ensure consistent size
                flattened_array = resized_image.flatten()

                # Write the image name and array to the CSV
                writer.writerow([image_file] + flattened_array.tolist())
                print(f"Processed and saved: {image_file}")
            except Exception as e:
                print(f"Error processing {image_file}: {e}")

# Usage
if __name__ == "__main__":
    input_folder = "path_to_your_input_folder"  # Replace with your folder path
    output_csv_path = "processed_images_256x256.csv"  # Replace with your desired output file name

    preprocess_folder(input_folder, output_csv_path)