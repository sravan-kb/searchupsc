from pdf2image import convert_from_path
pages = convert_from_path(
    r"C:\Users\srava\Downloads\2025UPSC\1page.pdf",
    dpi=300,
    poppler_path=r"C:\poppler\Library\bin"
)

pages[0].save(
    r"C:\Users\srava\Downloads\2025UPSC_PNG\page1.png",
    "PNG"
)
print("First page converted successfully")
