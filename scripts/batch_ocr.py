import pytesseract
from PIL import Image
import os

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Folder containing PNG images
image_folder = r"D:\Projects_CDAC\2025UPSC_PNG"

# Folder to save OCR text files
output_folder = r"D:\Projects_CDAC\2025UPSC_TXT"

# Loop through all PNG files
for filename in os.listdir(image_folder):

    # Process only PNG files
    if filename.endswith(".png"):

        # Full image path
        image_path = os.path.join(image_folder, filename)

        print(f"Processing: {filename}")

        # Open image
        img = Image.open(image_path)

        # Get image width and height
        width, height = img.size

        # Split into left and right columns
        left_column = img.crop((0, 0, width // 2, height))
        right_column = img.crop((width // 2, 0, width, height))

        # OCR left column
        left_text = pytesseract.image_to_string(left_column)

        # OCR right column
        right_text = pytesseract.image_to_string(right_column)

        # Combine OCR text
        final_text = left_text + "\n" + right_text

        # Create output TXT path
        output_path = os.path.join(
            output_folder,
            filename.replace(".png", ".txt")
        )

        # Save OCR text
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(final_text)

        print(f"Saved: {output_path}")

print("All OCR processing completed")