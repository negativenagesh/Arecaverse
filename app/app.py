import streamlit as st
import requests
from preprocessing import process_arecanut_image_steps
from utils import save_uploaded_file

# Set Streamlit page layout to wide
st.set_page_config(page_title="Arecanut Image Processing", layout="wide")

# Function to fetch agriculture news from NewsAPI
def get_agriculture_news():
    # NewsAPI key (replace with your own API key from https://newsapi.org/)
    api_key = 'ca52de44955649d0a2091e83010e777f'
    url = f"https://newsapi.org/v2/everything?q=agriculture+india&apiKey={"ca52de44955649d0a2091e83010e777f"}"
    
    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get('articles', [])
        return articles
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return []

# Streamlit App
st.title("Arecaverse")

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

# Create a two-column layout
col1, col2 = st.columns([3, 3])  # First column larger, second column (for news) smaller

# Column 2: Agriculture news (Placed at the top of col2)
with col2:
    st.header("Latest Agriculture News in India")
    
    # Get agriculture news
    articles = get_agriculture_news()
    
    if articles:
        for article in articles[:10]:  # Display top 5 articles
            st.subheader(article['title'])
            st.write(f"Source: {article['source']['name']}")
            st.write(f"[Read more]({article['url']})")
            st.write(article['description'])
            st.write("---")
    else:
        st.write("No news available at the moment.")

# Column 1: Main content (Arecanut Image processing)
with col1:
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