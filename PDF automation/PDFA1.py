import PyPDF2
from fpdf import FPDF
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_file = os.path.join(script_dir, "PDFA1.pdf")

# Open the PDF in read-binary mode
with open(pdf_file, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
