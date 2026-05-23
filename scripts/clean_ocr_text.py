import os
import re

# Folder containing OCR TXT files
input_folder = r"D:\Projects_CDAC\2025UPSC_TXT"

# Folder to save cleaned TXT files
output_folder = r"D:\Projects_CDAC\2025UPSC_CLEANED"

# OCR cleaning function
def clean_ocr_text(text):

    # Roman numeral fixes
    text = text.replace("\nL\n", "\nI.\n")
    text = text.replace("\nIl.\n", "\nII.\n")
    text = text.replace("Ill.", "III.")
    text = text.replace("lV", "IV")

    # Option formatting fixes
    text = text.replace("(a)\n\nI only", "(a) I only")
    text = text.replace("(b)\n(c)", "(b) ")
    text = text.replace("(a) 1, Il and I", "(d) I, II and III")

    # Common OCR mistakes
    text = text.replace(" Il ", " II ")
    text = text.replace(" I1 ", " II ")
    text = text.replace("Statementl", "Statement I")

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove excessive spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    return text

# Process all TXT files
for filename in os.listdir(input_folder):

    # Process only TXT files
    if filename.endswith(".txt"):

        # Full input path
        input_path = os.path.join(input_folder, filename)

        print(f"Cleaning: {filename}")

        # Read OCR text
        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Clean text
        cleaned_text = clean_ocr_text(text)

        # Output path
        output_path = os.path.join(output_folder, filename)

        # Save cleaned text
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(cleaned_text)

        print(f"Saved cleaned file: {output_path}")

print("All OCR text cleaned successfully")