import streamlit as st
import pytesseract as tess
from PIL import Image
import io
from collections import Counter
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob

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
    # Remove stop words
    custom_stopwords = set(ENGLISH_STOP_WORDS)
    words = re.findall(r'\b\w+\b', text.lower())
    words = [word for word in words if word not in custom_stopwords]

    # Filter out non-keywords based on specific conditions
    keywords = []
    for word in words:
        # Exclude single-character words and numeric values
        if len(word) > 3 and not word.isdigit():
            keywords.append(word)

    # Get word frequencies
    word_freq = Counter(keywords)

    # Get top 30 keywords based on frequency
    top_keywords = [word for word, freq in word_freq.most_common(30)]
    return top_keywords, word_freq

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    st.title("Image2Text Analyzer")
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://example.com/background_image.jpg");
            background-size: cover;
        }
        .sidebar .sidebar-content {
            background: linear-gradient(to right, #b3ffab, #12fff7);
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Upload Image
    st.header("Choose an image...")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)

        # Button to trigger text extraction
        if st.button("Extract Text"):
            # Extract text from image
            extracted_text = extract_text(image)

            if extracted_text:
                # Analyze sentiment of extracted text
                sentiment = analyze_sentiment(extracted_text)
                st.subheader(f"Sentiment: {sentiment}")

                # Provide a download link for the extracted text and keywords
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="Download Extracted Text",
                        data=extracted_text,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )
                with col2:
                    # Extract keywords from extracted text
                    keywords, word_freq = extract_keywords(extracted_text)
                    keywords_text = "\n".join(keywords)
                    st.download_button(
                        label="Download Keywords",
                        data=keywords_text,
                        file_name="extracted_keywords.txt",
                        mime="text/plain"
                    )

if __name__ == "__main__":
    main()
