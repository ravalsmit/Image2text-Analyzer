import streamlit as st
import pytesseract as tess
from PIL import Image
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Set path to Tesseract executable
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image):
    try:
        text = tess.image_to_string(image)
        return text.strip()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.warning("Please try uploading another image or check your internet connection.")
        return None

def extract_keywords(text):
    # Define custom stop words
    custom_stopwords = list(ENGLISH_STOP_WORDS) + ["example", "words", "to", "remove", "from", "keywords"]

    # Extract keywords using TF-IDF
    tfidf_vectorizer = TfidfVectorizer(stop_words=custom_stopwords)
    tfidf_matrix = tfidf_vectorizer.fit_transform([text])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]

    # Sort the features based on TF-IDF scores
    sorted_indices = scores.argsort()[::-1]
    top_keywords = [feature_names[i] for i in sorted_indices[:10]]  # Extract top 10 keywords
    return top_keywords

def main():
    st.title("Image Text Extractor and Keyword Extractor")

    # Upload Image
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.subheader("Uploaded Image")
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Button to trigger text extraction
        if st.button("Extract Text"):
            st.info("Extracting text... This may take a moment.")

            # Extract text from image
            extracted_text = extract_text(image)

            if extracted_text:
                st.success("Text extraction successful!")
                # Display extracted text
                st.subheader("Extracted Text")
                st.text(extracted_text)

                # Extract keywords from extracted text
                keywords = extract_keywords(extracted_text)
                st.subheader("Keywords Extracted")
                st.write(keywords)

if __name__ == "__main__":
    main()
