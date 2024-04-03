import streamlit as st
import pytesseract as tess
from PIL import Image
import io
from collections import Counter
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

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

def main():
    st.title("Image Text Extractor and Keyword Extractor")

    # Upload Image
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.subheader("Uploaded Image")
        image = Image.open(uploaded_file)

        # Button to trigger text extraction
        if st.button("Extract Text"):
            # Extract text from image
            extracted_text = extract_text(image)

            if extracted_text:
                # Provide a download link for the extracted text and keywords
                st.subheader("Download Extracted Text and Keywords")
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

                # Visualization: Word cloud of keywords
                st.subheader("Keyword Word Cloud")
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
                plt.figure(figsize=(10, 6))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                st.pyplot(plt.gcf())  # Pass the current figure to st.pyplot()

if __name__ == "__main__":
    main()
