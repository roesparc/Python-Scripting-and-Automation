import PyPDF2
from fpdf import FPDF
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_output = os.path.join(script_dir, "PDFA2.pdf")

# Create a PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12)
pdf.cell(200, 20, text="Hello World!", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.output(pdf_output)
