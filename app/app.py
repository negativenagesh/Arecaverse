import streamlit as st
from preprocessing import process_arecanut_image
from utils import save_uploaded_file


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
            # Save uploaded file
            temp_file_path = save_uploaded_file(uploaded_file)

            # Process the temporary file
            output_folder = "output/"
            output_path = process_arecanut_image(temp_file_path, output_folder)

            # Display the processed image
            st.image(output_path, caption="Processed Image", use_column_width=True)
            st.success("Image processed successfully!")
        except Exception as e:
            st.error(f"Error: {e}")