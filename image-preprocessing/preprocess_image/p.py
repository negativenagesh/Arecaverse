import cv2
import numpy as np
from rembg import remove
import os

def process_images_in_folder(input_folder, output_folder):
    """
    Processes all images in a folder by performing the following steps:
    1. Removes the background.
    2. Resizes to 256x256.
    3. Converts to grayscale.
    4. Applies CLAHE.
    5. Sharpens the image.
    6. Computes the Sobel gradient magnitude.

    Saves the processed images in the output folder.

    Parameters:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder where processed images will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # List all image files in the folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        raise ValueError(f"No images found in the folder: {input_folder}")

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        try:
            # Step 1: Read the image
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"Unable to read the image: {image_file}")

            # Step 2: Remove Background
            _, buffer = cv2.imencode(".png", img)
            output_data = remove(buffer.tobytes())
            bg_removed_img = cv2.imdecode(np.frombuffer(output_data, np.uint8), cv2.IMREAD_UNCHANGED)

            # Step 3: Resize to 256x256
            resized_img = cv2.resize(bg_removed_img, (128, 128))

            # Step 4: Convert to Grayscale
            gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

            # Step 5: Apply CLAHE
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            clahe_img = clahe.apply(gray_img)

            # Save the final processed image
            output_image_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_image_path, clahe_img)

            print(f"Processed and saved: {image_file}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

# # Usage
# if __name__ == "__main__":
#     input_folder = "/content/areca-nut/arecanut/1stchali"  # Replace with your folder path
#     output_folder = "/content/1stchalipreprocessed"  # Replace with your desired output folder path

#     process_images_in_folder(input_folder, output_folder)

# if __name__ == "__main__":
#     input_folder = "/content/areca-nut/arecanut/Gotu"  # Replace with your folder path
#     output_folder = "/content/Gotupreprocessed"  # Replace with your desired output folder path

#     process_images_in_folder(input_folder, output_folder)
  
if __name__ == "__main__":
    input_folder = "/content/areca-nut/arecanut/Kole"  # Replace with your folder path
    output_folder = "/content/kolepreprocessed"  # Replace with your desired output folder path

    process_images_in_folder(input_folder, output_folder)
