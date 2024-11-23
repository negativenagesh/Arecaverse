import streamlit as st
from preprocessing import process_arecanut_image_steps
from utils import save_uploaded_file


# Streamlit App
st.title("Arecanut Image Processing App")

st.write(
    """
    This app allows you to upload an arecanut image and processes it through the following steps:
    - Removes the background.
    - Resizes the image to 128x128.
    - Converts the image to grayscale.
    - Applies CLAHE for contrast enhancement.
    - Applies sharpening.
    - Computes Sobel gradient magnitude.
    """
)

# Upload file
uploaded_file = st.file_uploader("Upload an Arecanut Image", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Process Image"):
        try:
            # Save uploaded file temporarily
            temp_file_path = save_uploaded_file(uploaded_file)

            # Process the image step by step
            steps = process_arecanut_image_steps(temp_file_path)

            # Display each processing step
            for step_name, step_image in steps.items():
                st.subheader(step_name)
                st.image(step_image, use_column_width=True)

            st.success("Image processed successfully!")
        except Exception as e:
            st.error(f"Error: {e}")