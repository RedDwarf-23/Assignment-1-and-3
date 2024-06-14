# Table extraction 
Extracting tables from an image


Install latest version of Tesseract on the local computer:
url: https://github.com/UB-Mannheim/tesseract/wiki

Install the various libraries in the requirements.text file

Install:
1. pip install Pillow
2. pip install tesseract
3. pip install jinja2==3.1.2
 
Add this line of code:

pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe' # your path may be different


