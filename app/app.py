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
    url = f"https://newsapi.org/v2/everything?q=agriculture+india&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get('articles', [])
        return articles
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return []

# Streamlit App

# Center the title with bold styling and larger font size
st.markdown(
    """
    <style>
    .title-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .title-container img {
        margin-right: 10px;
    }
    .nav-bar {
        display: flex;
        gap: 20px;
    }
    .nav-bar button, .nav-bar a {
        background-color: transparent;
        color: #4CAF50;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
    .nav-bar a img {
        vertical-align: middle;
        width: 20px;
        height: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-container">
        <div style="display: flex; align-items: center;">
            <img src="/workspaces/Arecanut-quality-classification/app/arecanut-logo.png" width="50">
            <h1 style='font-weight: bold; font-size: 3em; margin: 0;'>Arecaverse</h1>
        </div>
        <div class="nav-bar">
            <button onclick="window.location.href='#about'">About</button>
            <button onclick="window.location.href='#careers'">Careers</button>
            <button onclick="window.location.href='#contact'">Contact</button>
            <button onclick="window.location.href='#login'">Login / Signup</button>
            <a href="https://github.com/your-repo" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub">
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Create a two-column layout at the top for introduction and news
col1, col2 = st.columns([2, 1])  # Adjust widths as needed

# Column 1: Arecaverse Title and Intro
with col1:
    with st.expander("Arecanut Image Processing", expanded=True):
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

# Column 2: Agriculture News
with col2:
    with st.expander("Latest Agriculture News in India", expanded=True):
        st.subheader("Latest Agriculture News in India")
        
        # Get agriculture news
        articles = get_agriculture_news()
        
        if articles:
            for article in articles[:30]:  # Limit displayed articles to the top 30
                st.markdown(f"**{article['title']}**")
                st.write(f"Source: {article['source']['name']}")
                st.write(f"[Read more]({article['url']})")
                st.write("---")
        else:
            st.write("No news available at the moment.")