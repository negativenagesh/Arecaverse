import os
from dotenv import load_dotenv
import streamlit as st
import requests
from preprocessing import process_arecanut_image_steps
from utils import save_uploaded_file

load_dotenv()

# Set Streamlit page layout to wide
st.set_page_config(page_title="Arecanut Image Processing", layout="wide")

# Translation dictionary
translations = {
    "English": {
        "title": "Arecanut Image Processing and Quality classification",
        "upload": "Upload an Arecanut Image",
        "process": "Process Image",
        "weather_info": "Weather Information",
        "enter_location": "Enter location for weather",
        "get_weather": "Get Weather",
        "news": "Latest Agriculture News in India",
        "see_more_news": "See More News",
        "about": "About",
        "careers": "Careers",
        "contact": "Contact",
        "login_signup": "Login / Signup",
        "intro": "This app allows you to upload an arecanut image and processes it through the following steps:",
        "step1": "Removes the background.",
        "step2": "Resizes the image to 128x128.",
        "step3": "Converts the image to grayscale.",
        "step4": "Applies CLAHE for contrast enhancement.",
        "step5": "Applies sharpening.",
        "step6": "Computes Sobel gradient magnitude.",
        "drag_drop": "Drag and drop file here",
        "limit": "Limit 200MB per file • JPG, JPEG, PNG, BMP, TIFF, WEBP, TIF"
    },
    "हिन्दी": {
        "title": "अरेकेनट छवि प्रसंस्करण और गुणवत्ता वर्गीकरण",
        "upload": "एक अरेकेनट छवि अपलोड करें",
        "process": "छवि संसाधित करें",
        "weather_info": "मौसम की जानकारी",
        "enter_location": "मौसम के लिए स्थान दर्ज करें",
        "get_weather": "मौसम प्राप्त करें",
        "news": "भारत में नवीनतम कृषि समाचार",
        "see_more_news": "अधिक समाचार देखें",
        "about": "के बारे में",
        "careers": "करियर",
        "contact": "संपर्क करें",
        "login_signup": "लॉगिन / साइनअप",
        "intro": "यह ऐप आपको एक अरेकेनट छवि अपलोड करने और निम्नलिखित चरणों के माध्यम से इसे संसाधित करने की अनुमति देता है:",
        "step1": "पृष्ठभूमि को हटा देता है।",
        "step2": "छवि का आकार 128x128 में बदलता है।",
        "step3": "छवि को ग्रेस्केल में बदलता है।",
        "step4": "कॉन्ट्रास्ट वृद्धि के लिए CLAHE लागू करता है।",
        "step5": "शार्पनिंग लागू करता है।",
        "step6": "सोबेल ग्रेडिएंट परिमाण की गणना करता है।",
        "drag_drop": "यहां फ़ाइल खींचें और छोड़ें",
        "limit": "प्रति फ़ाइल 200MB की सीमा • JPG, JPEG, PNG, BMP, TIFF, WEBP, TIF"
    },
    "ಕನ್ನಡ": {
        "title": "ಅರೆಕನಟ್ ಚಿತ್ರ ಸಂಸ್ಕರಣೆ ಮತ್ತು ಗುಣಮಟ್ಟ ವರ್ಗೀಕರಣ",
        "upload": "ಅರೆಕನಟ್ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ",
        "process": "ಚಿತ್ರವನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ",
        "weather_info": "ಹವಾಮಾನ ಮಾಹಿತಿ",
        "enter_location": "ಹವಾಮಾನಕ್ಕಾಗಿ ಸ್ಥಳವನ್ನು ನಮೂದಿಸಿ",
        "get_weather": "ಹವಾಮಾನ ಪಡೆಯಿರಿ",
        "news": "ಭಾರತದಲ್ಲಿ ಇತ್ತೀಚಿನ ಕೃಷಿ ಸುದ್ದಿ",
        "see_more_news": "ಇನ್ನಷ್ಟು ಸುದ್ದಿಗಳನ್ನು ನೋಡಿ",
        "about": "ಬಗ್ಗೆ",
        "careers": "ವೃತ್ತಿಗಳು",
        "contact": "ಸಂಪರ್ಕಿಸಿ",
        "login_signup": "ಲಾಗಿನ್ / ಸೈನ್ ಅಪ್",
        "intro": "ಈ ಅಪ್ಲಿಕೇಶನ್ ನಿಮಗೆ ಅರೆಕನಟ್ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು ಮತ್ತು ಕೆಳಗಿನ ಹಂತಗಳ ಮೂಲಕ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಅನುಮತಿಸುತ್ತದೆ:",
        "step1": "ಹಿನ್ನೆಲೆಯನ್ನು ತೆಗೆದುಹಾಕುತ್ತದೆ.",
        "step2": "ಚಿತ್ರದ ಗಾತ್ರವನ್ನು 128x128 ಗೆ ಬದಲಾಯಿಸುತ್ತದೆ.",
        "step3": "ಚಿತ್ರವನ್ನು ಗ್ರೇಸ್ಕೇಲ್ ಗೆ ಪರಿವರ್ತಿಸುತ್ತದೆ.",
        "step4": "ವಿರೋಧಾಭಾಸ ಹೆಚ್ಚಿಸಲು CLAHE ಅನ್ನು ಅನ್ವಯಿಸುತ್ತದೆ.",
        "step5": "ಶಾರ್ಪನಿಂಗ್ ಅನ್ನು ಅನ್ವಯಿಸುತ್ತದೆ.",
        "step6": "ಸೊಬೆಲ್ ಗ್ರೇಡಿಯಂಟ್ ಪರಿಮಾಣವನ್ನು ಲೆಕ್ಕಹಾಕುತ್ತದೆ.",
        "drag_drop": "ಫೈಲ್ ಅನ್ನು ಇಲ್ಲಿ ಎಳೆಯಿರಿ ಮತ್ತು ಬಿಡಿ",
        "limit": "ಪ್ರತಿ ಫೈಲ್ 200MB ಮಿತಿ • JPG, JPEG, PNG, BMP, TIFF, WEBP, TIF"
    },
    "മലയാളം": {
        "title": "അരികനട്ട് ചിത്രം പ്രോസസ്സിംഗ്  ഗുണനിലവാര വർഗ്ഗീകരണം",
        "upload": "ഒരു അരികനട്ട് ചിത്രം അപ്ലോഡ് ചെയ്യുക",
        "process": "ചിത്രം പ്രോസസ്സ് ചെയ്യുക",
        "weather_info": "കാലാവസ്ഥാ വിവരം",
        "enter_location": "കാലാവസ്ഥയ്ക്ക് സ്ഥലം നൽകുക",
        "get_weather": "കാലാവസ്ഥ നേടുക",
        "news": "ഇന്ത്യയിലെ ഏറ്റവും പുതിയ കൃഷി വാർത്തകൾ",
        "see_more_news": "കൂടുതൽ വാർത്തകൾ കാണുക",
        "about": "കുറിച്ച്",
        "careers": "തൊഴിൽ",
        "contact": "ബന്ധപ്പെടുക",
        "login_signup": "ലോഗിൻ / സൈൻ അപ്പ്",
        "intro": "ഈ ആപ്പ് നിങ്ങളെ ഒരു അരികനട്ട് ചിത്രം അപ്ലോഡ് ചെയ്യാനും താഴെ പറയുന്ന ഘട്ടങ്ങളിലൂടെ പ്രോസസ്സ് ചെയ്യാനും അനുവദിക്കുന്നു:",
        "step1": "പശ്ചാത്തലം നീക്കം ചെയ്യുന്നു.",
        "step2": "ചിത്രത്തിന്റെ വലുപ്പം 128x128 ആയി മാറ്റുന്നു.",
        "step3": "ചിത്രം ഗ്രേസ്കെയിലിലേക്ക് മാറ്റുന്നു.",
        "step4": "കോണ്ട്രാസ്റ്റ് വർദ്ധനവിനായി CLAHE പ്രയോഗിക്കുന്നു.",
        "step5": "ഷാർപ്പനിംഗ് പ്രയോഗിക്കുന്നു.",
        "step6": "സോബൽ ഗ്രേഡിയന്റ് മാഗ്നിറ്റ്യൂഡ് കണക്കാക്കുന്നു.",
        "drag_drop": "ഫയൽ ഇവിടെ വലിച്ചിടുക",
        "limit": "ഓരോ ഫയലിനും 200MB പരിധി • JPG, JPEG, PNG, BMP, TIFF, WEBP, TIF"
    },
    "తెలుగు": {
        "title": "అరికెనట్ చిత్రం ప్రాసెసింగ్ మరియు నాణ్యత వర్గీకరణ",
        "upload": "ఒక అరికెనట్ చిత్రాన్ని అప్‌లోడ్ చేయండి",
        "process": "చిత్రాన్ని ప్రాసెస్ చేయండి",
        "weather_info": "వాతావరణ సమాచారం",
        "enter_location": "వాతావరణానికి స్థలాన్ని నమోదు చేయండి",
        "get_weather": "వాతావరణాన్ని పొందండి",
        "news": "భారతదేశంలో తాజా వ్యవసాయ వార్తలు",
        "see_more_news": "మరిన్ని వార్తలు చూడండి",
        "about": "గురించి",
        "careers": "కెరీర్స్",
        "contact": "సంప్రదించండి",
        "login_signup": "లాగిన్ / సైన్ అప్",
        "intro": "ఈ యాప్ మీకు ఒక అరికెనట్ చిత్రాన్ని అప్‌లోడ్ చేయడానికి మరియు క్రింది దశల ద్వారా ప్రాసెస్ చేయడానికి అనుమతిస్తుంది:",
        "step1": "పశ్చాత్తాపాన్ని తొలగిస్తుంది.",
        "step2": "చిత్రాన్ని 128x128 కి పరిమాణం చేస్తుంది.",
        "step3": "చిత్రాన్ని గ్రేస్కేల్ కి మార్చుతుంది.",
        "step4": "కాంట్రాస్ట్ పెంపు కోసం CLAHE ని అన్వయిస్తుంది.",
        "step5": "షార్పనింగ్ ని అన్వయిస్తుంది.",
        "step6": "సోబెల్ గ్రేడియంట్ పరిమాణాన్ని లెక్కిస్తుంది.",
        "drag_drop": "ఫైల్‌ను ఇక్కడ డ్రాగ్ చేసి డ్రాప్ చేయండి",
        "limit": "ప్రతి ఫైల్ 200MB పరిమితి • JPG, JPEG, PNG, BMP, TIFF, WEBP, TIF"
    },
    "தமிழ்": {
        "title": "அரைக்காடு படம் செயலாக்கம் மற்றும் தர வகைப்படுத்தல்",
        "upload": "ஒரு அரைக்காடு படத்தை பதிவேற்றவும்",
        "process": "படத்தை செயலாக்கவும்",
        "weather_info": "வானிலை தகவல்",
        "enter_location": "வானிலைக்கு இடத்தை உள்ளிடவும்",
        "get_weather": "வானிலை பெறவும்",
        "news": "இந்தியாவில் சமீபத்திய வேளாண்மை செய்திகள்",
        "see_more_news": "மேலும் செய்திகள் காண்க",
        "about": "பற்றி",
        "careers": "வேலைவாய்ப்புகள்",
        "contact": "தொடர்பு கொள்ளவும்",
        "login_signup": "உள்நுழைவு / பதிவு",
        "intro": "இந்த பயன்பாடு உங்களுக்கு ஒரு அரைக்காடு படத்தை பதிவேற்றவும் மற்றும் கீழ்க்கண்ட படிநிலைகளின் மூலம் செயலாக்கவும் அனுமதிக்கிறது:",
        "step1": "பின்னணியை அகற்றுகிறது.",
        "step2": "படத்தை 128x128 ஆக மாற்றுகிறது.",
        "step3": "படத்தை கிரேஸ்கேலாக மாற்றுகிறது.",
        "step4": "எதிர்மறை அதிகரிப்புக்கு CLAHE ஐப் பயன்படுத்துகிறது.",
        "step5": "கூர்மையைப் பயன்படுத்துகிறது.",
        "step6": "சோபெல் சாய்வு அளவை கணக்கிடுகிறது.",
        "drag_drop": "கோப்பை இங்கே இழுத்து விடவும்",
        "limit": "ஒவ்வொரு கோப்புக்கும் 200MB வரம்பு • JPG, JPEG, PNG, BMP, TIFF, WEBP, TIF"
    },
    "日本語": {
        "title": "アレカナット画像処理と品質分類",
        "upload": "アレカナット画像をアップロード",
        "process": "画像を処理",
        "weather_info": "天気情報",
        "enter_location": "天気のために場所を入力",
        "get_weather": "天気を取得",
        "news": "インドの最新農業ニュース",
        "see_more_news": "もっとニュースを見る",
        "about": "約",
        "careers": "キャリア",
        "contact": "連絡先",
        "login_signup": "ログイン / サインアップ",
        "intro": "このアプリでは、アレカナット画像をアップロードし、以下のステップで処理することができます:",
        "step1": "背景を削除します。",
        "step2": "画像を128x128にリサイズします。",
        "step3": "画像をグレースケールに変換します。",
        "step4": "コントラスト強調のためにCLAHEを適用します。",
        "step5": "シャープ化を適用します。",
        "step6": "ソーベル勾配の大きさを計算します。",
        "drag_drop": "ここにファイルをドラッグ＆ドロップ",
        "limit": "ファイルごとに200MBの制限 • JPG, JPEG, PNG, BMP, TIFF, WEBP, TIF"
    }
}

# Function to fetch agriculture news from NewsAPI
def get_agriculture_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q=agriculture+india&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get('articles', [])
        return articles
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return []

# Function to fetch weather information
def get_weather(location):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"
    
    try:
        response = requests.get(url)
        weather_data = response.json()
        if "error" in weather_data:
            st.error(weather_data["error"].get("info", "Error fetching weather data"))
            return None
        return weather_data
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit App

# Language Selection
language = st.selectbox("Translate", ["English", "हिन्दी", "ಕನ್ನಡ", "മലയാളം", "తెలుగు", "தமிழ்", "日本語"])

# Get translations for the selected language
trans = translations[language]

# Center the title with bold styling and larger font size
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
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
        font-size: 18px;  /* Decreased font size */
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
    .nav-bar a img {
        vertical-align: middle;
        width: 25px;  /* Decreased width */
        height: 25px;  /* Decreased height */
        background-color: transparent;  /* Remove white background */
    }
    .footer {
        background-color: #333;
        color: white;
        padding: 20px;
        text-align: center;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
    }
    .footer a {
        color: #4CAF50;
        text-decoration: none;
    }
    .footer a img {
        vertical-align: middle;
        width: 30px;
        height: 30px;
    }
    .stButton button {
        color: black;  /* Set button text color to black */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="title-container">
        <div style="display: flex; align-items: center;">
            <img src="/workspaces/Arecanut-quality-classification/app/arecanut-logo.png" width="50">
            <h1 style='font-weight: bold; font-size: 3em; margin: 0;'>Arecaverse</h1>
        </div>
        <div class="nav-bar">
            <a href="https://github.com/negativenagesh/Arecanut-quality-classification/blob/main/README.md"><button>{trans["about"]}</button></a>
            <button onclick="window.location.href='#careers'">{trans["careers"]}</button>
            <a href="mailto:gaonkarsub@gmail.com"><button>{trans["contact"]}</button></a>
            <button onclick="window.location.href='#login'">{trans["login_signup"]}</button>
            <a href="https://github.com/negativenagesh/Arecanut-quality-classification" target="_blank">
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
    with st.expander(trans["title"], expanded=True):
        st.write(trans["intro"])
        st.write(f"- {trans['step1']}")
        st.write(f"- {trans['step2']}")
        st.write(f"- {trans['step3']}")
        st.write(f"- {trans['step4']}")
        st.write(f"- {trans['step5']}")
        st.write(f"- {trans['step6']}")

        uploaded_file = st.file_uploader(trans["upload"], type=["jpg", "jpeg", "png", "bmp", "tiff", "webp"], help=f"{trans['drag_drop']} • {trans['limit']}")

        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

            if st.button(trans["process"]):
                try:
                    # Save uploaded file temporarily
                    temp_file_path = save_uploaded_file(uploaded_file)

                    # Process the image step by step
                    steps = process_arecanut_image_steps(temp_file_path)

                    # Display each processing step
                    for step_name, step_image in steps.items():
                        st.subheader(step_name)
                        st.image(step_image, use_container_width=True)

                    st.success("Image processed successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")

# Column 2: Weather Information
with col2:
    with st.expander(trans["weather_info"], expanded=True):
        st.subheader(trans["weather_info"])
        location = st.text_input(trans["enter_location"], "Bengaluru")
        if st.button(trans["get_weather"]):
            weather = get_weather(location)
            if weather:
                st.markdown(f"**Location:** {weather['location']['name']}, {weather['location']['region']}")
                st.markdown(f"**Temperature:** {weather['current']['temperature']}°C")
                st.markdown(f"**Condition:** {weather['current']['weather_descriptions'][0]}")
                st.markdown(f"**Wind Speed:** {weather['current']['wind_speed']} km/h")
                st.markdown(f"**Wind Direction:** {weather['current']['wind_dir']}")
                st.markdown(f"**Humidity:** {weather['current']['humidity']}%")
                st.markdown(f"**UV Index:** {weather['current']['uv_index']}")
                st.markdown(f"**Observation Time:** {weather['current']['observation_time']}")
                st.markdown(f"**Local Time:** {weather['location']['localtime']}")

# Column 2: Agriculture News
with col2:
    with st.expander(trans["news"], expanded=True):
        st.subheader(trans["news"])
        
        # Get agriculture news
        articles = get_agriculture_news()
        
        if articles:
            for article in articles[:10]:  # Limit displayed articles to the top 10
                st.markdown(f"**{article['title']}**")
                st.write(f"Source: {article['source']['name']}")
                st.write(f"[Read more]({article['url']})")
                st.write("---")
            
            if len(articles) > 10:
                if st.button(trans["see_more_news"]):
                    for article in articles[10:15]:
                        st.markdown(f"**{article['title']}**")
                        st.write(f"Source: {article['source']['name']}")
                        st.write(f"[Read more]({article['url']})")
                        st.write("---")
        else:
            st.write("No news available at the moment.")

# Footer
st.markdown(
    f"""
    <div class="footer">
        <p>&copy; 2024 Arecaverse. All rights reserved.</p>
        <p>
            <a href="https://github.com/negativenagesh/Arecanut-quality-classification" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub">
            </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)