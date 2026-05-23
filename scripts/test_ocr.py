import pytesseract
from PIL import Image

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
img = Image.open(
    r"C:\Users\srava\Downloads\2025UPSC_PNG\page1.png"
)

# Extract text using OCR
text = pytesseract.image_to_string(img)

# Print extracted text
print(text)