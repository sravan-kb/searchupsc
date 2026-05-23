from pdf2image import convert_from_path
import os

# Folder containing single-page PDFs
pdf_folder = (
    r"D:\Projects_CDAC\2025UPSC\Extract oddpages upsc 2025"
)

# Folder to save PNG images
output_folder = r"D:\Projects_CDAC\2025UPSC_PNG"

# Poppler path
poppler_path = r"C:\poppler\Library\bin"

# Loop through all PDF files
for filename in os.listdir(pdf_folder):

    # Process only PDFs
    if filename.endswith(".pdf"):

        # Full PDF path
        pdf_path = os.path.join(pdf_folder, filename)

        print(f"Processing: {filename}")

        # Convert PDF to image
        pages = convert_from_path(
            pdf_path,
            dpi=300,
            poppler_path=poppler_path
        )

        # Create output PNG filename
        output_path = os.path.join(
            output_folder,
            filename.replace(".pdf", ".png")
        )

        # Save first page as PNG
        pages[0].save(output_path, "PNG")

        print(f"Saved: {output_path}")

print("All PDFs converted successfully")