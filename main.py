import re
import difflib
import streamlit as st
import pytesseract as tess

from PIL import Image
from textblob import TextBlob
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Set path to Tesseract executable
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"


def extract_text(image):
    try:
        text = tess.image_to_string(image)
        return text.strip()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.warning("Please try uploading another image or check your internet connection.")
        return None


def spell_check(text):
    words = re.findall(r'\b\w+\b', text.lower())
    corrected_text = []
    for word in words:
        corrected_word = difflib.get_close_matches(word, ENGLISH_STOP_WORDS, n=1)
        corrected_text.append(corrected_word[0] if corrected_word else word)
    return ' '.join(corrected_text)


def extract_keywords(text):
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Remove stop words
    custom_stopwords = set(ENGLISH_STOP_WORDS)
    words = [word for word in words if word not in custom_stopwords]

    # Filter out non-keywords based on specific conditions
    keywords = [word for word in words if len(word) > 3 and not word.isdigit()]

    # Get word frequencies
    word_freq = Counter(keywords)

    # Get top 30 keywords based on frequency
    top_keywords = [word for word, freq in word_freq.most_common(30)]

    return top_keywords, word_freq


def main():
    st.title("Image2Text Analyzer")

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
                # Perform spell-checking
                corrected_text = spell_check(extracted_text)
                # st.write("Corrected Text:")
                # st.write(corrected_text)

                # Analyze sentiment of corrected text
                sentiment = analyze_sentiment(corrected_text)
                st.subheader(f"Sentiment: {sentiment}")

                # Provide a download link for the extracted text and keywords
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.download_button(
                        label="Download Extracted Text",
                        data=extracted_text,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )
                with col2:
                    st.download_button(
                        label="Download Corrected Text",
                        data=corrected_text,
                        file_name="corrected_text.txt",
                        mime="text/plain"
                    )
                with col3:
                    # Extract keywords from extracted text
                    keywords, word_freq = extract_keywords(corrected_text)
                    keywords_text = "\n".join(keywords)
                    st.download_button(
                        label="Download Keywords",
                        data=keywords_text,
                        file_name="extracted_keywords.txt",
                        mime="text/plain"
                    )


if __name__ == "__main__":
    main()
