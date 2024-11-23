import tempfile

def save_uploaded_file(uploaded_file):
    """
    Saves a Streamlit uploaded file to a temporary location.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        return temp_file.name