import streamlit as st
import pytesseract as tess
from PIL import Image

# Set path to Tesseract executable
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def main():
    st.title("Resume Text Extractor")

    # Upload Image
    st.header("Upload Resume Image")
    uploaded_file = st.file_uploader("Choose a resume image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Resume", use_column_width=True)

        # Extract text from image
        text = tess.image_to_string(image)

        # Display extracted text
        st.header("Extracted Text")
        st.text(text)


if __name__ == "__main__":
    main()