# Image2Text Analyzer

Image2Text Analyzer is a Streamlit web application that allows users to upload images containing text, extract the text using Tesseract OCR, perform spell-checking, sentiment analysis, and extract keywords from the extracted text.

## Features

- **Text Extraction**: Upload an image and extract text using Tesseract OCR.
- **Spell Checking**: Perform spell-checking on the extracted text to correct any misspelled words.
- **Sentiment Analysis**: Analyze the sentiment of the extracted and corrected text (positive, negative, or neutral).
- **Keyword Extraction**: Extract keywords from the corrected text based on word frequencies.

## Usage

1. **Upload Image**: Click on the "Choose an image..." button to upload an image containing text.
2. **Extract Text**: After uploading the image, click on the "Extract Text" button to extract text from the image.
3. **View Results**: Once the text is extracted, the sentiment analysis result will be displayed, and you can download the extracted text, corrected text, and extracted keywords.

## Installation

1. Clone the repository: git clone https://github.com/ravalsmit/image2text-analyzer.git
2. Navigate to the project directory: cd Image2Text-Analyzer
3. Install dependencies: pip install -r requirements.txt

## Run

To run the application, execute the following command: streamlit run main.py

## Technologies Used:
- Streamlit: For building the web application.
- PyTesseract: For OCR.
- TextBlob: For sentiment analysis.

## Dependencies

- `streamlit`: 0.87.0
- `pytesseract`: 0.3.8
- `pillow`: 8.4.0
- `scikit-learn`: 0.24.2
- `textblob`: 0.15.3

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
