import os
import cv2
import numpy as np
from rembg import remove
from PIL import Image
import streamlit as st
import tempfile


def process_arecanut_image(input_image_path, output_folder):
    """
    Combines the steps of converting images to .png, removing backgrounds,
    and preprocessing the images.
    """
    os.makedirs(output_folder, exist_ok=True)

    try:
        # Read the image file
        with open(input_image_path, "rb") as img_file:
            input_data = img_file.read()

        # Remove background
        output_data = remove(input_data)
        temp_path = os.path.join(output_folder, "temp_image.png")

        with open(temp_path, "wb") as out_file:
            out_file.write(output_data)

        # Preprocess the background-removed image
        img = cv2.imread(temp_path)

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

        sobelx = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=3)

        gradient_magnitude = np.hypot(sobelx, sobely)
        gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))

        normalized_img = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
        normalized_img = np.uint8(normalized_img)

        output_path = os.path.join(output_folder, "processed_image.png")
        cv2.imwrite(output_path, normalized_img)

        return output_path
    except Exception as e:
        raise ValueError(f"Error processing the image: {e}")


# Streamlit App
st.title("Arecanut Image Processing App")

st.write(
    """
    This app allows you to upload an arecanut image and processes it through the following steps:
    - Converts the image to PNG format.
    - Removes the background.
    - Preprocesses the image (resizing, grayscale, CLAHE, sharpening, and Sobel gradient).
    """
)

# Upload file
uploaded_file = st.file_uploader("Upload an Arecanut Image", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Process Image"):
        try:
            # Use a temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                temp_file.write(uploaded_file.getbuffer())
                temp_file_path = temp_file.name

            # Process the temporary file
            output_folder = "output/"
            output_path = process_arecanut_image(temp_file_path, output_folder)

            # Display the processed image
            st.image(output_path, caption="Processed Image", use_column_width=True)
            st.success("Image processed successfully!")
        except Exception as e:
            st.error(f"Error: {e}")