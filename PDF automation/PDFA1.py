import PyPDF2
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_file = os.path.join(script_dir, "PDFA1.pdf")
output_file = os.path.join(script_dir, "PDFA1_text.txt")

# Open the PDF in read-binary mode
with open(pdf_file, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    all_text = []

    # Loop through all pages and extract text
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            all_text.append(f"--- Page {i+1} ---\n{text}\n")

    # Save extracted text to a .txt file
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(all_text)
