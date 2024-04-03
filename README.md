## Overview
Image2Text Analyzer is a web application that extracts text from images using OCR (Optical Character Recognition) and performs text analysis, including sentiment analysis and keyword extraction.

## Features:
- Text Extraction: Upload an image containing text, and the app will extract the text using OCR.
- Sentiment Analysis: Analyze the sentiment of the extracted text (Positive, Negative, Neutral).
- Keyword Extraction: Extract keywords from the text and visualize their frequency.
- Customizable Plots: Choose which plots to display based on user preferences.

## Usage:
1. Upload Image: Choose an image containing text.
2. Extract Text: Extract text from the uploaded image.
3. View Analysis: See sentiment analysis, download extracted text and keywords, and view selected plots.

## Installation:
1. Clone the repository: git clone https://github.com/ravalsmit/image2text-analyzer.git
2. Navigate to the project directory: cd image2text-analyzer
3. Install dependencies: pip install -r requirements.txt

## Run:
Run the Streamlit app: streamlit run app.py

## Technologies Used:
- Streamlit: For building the web application.
- PyTesseract: For OCR.
- TextBlob: For sentiment analysis.

## Contributing:
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License:
This project is licensed under the MIT License. See the LICENSE file for details.
