import pytesseract
from PIL import Image

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Load image
img = Image.open(
    r"C:\Users\srava\Downloads\2025UPSC_PNG\page1.png"
)

# Get image width and height
width, height = img.size

print("Width:", width)
print("Height:", height)

# Split image into left and right columns
left_column = img.crop((0, 0, width // 2, height))
right_column = img.crop((width // 2, 0, width, height))

# OCR left column
left_text = pytesseract.image_to_string(left_column)

# OCR right column
right_text = pytesseract.image_to_string(right_column)

# Combine text
final_text = left_text + "\n" + right_text

# Print final text
print(final_text)