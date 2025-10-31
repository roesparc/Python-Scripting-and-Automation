from fpdf import FPDF
import os

# Sample data (could come from a database, CSV, or Excel)
report_data = [
    {"item": "Apples", "qty": 10, "price": 0.5},
    {"item": "Oranges", "qty": 5, "price": 0.8},
    {"item": "Bananas", "qty": 7, "price": 0.3},
]

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_output = os.path.join(script_dir, "PDFA2.pdf")

# Create PDF
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("helvetica", "B", 24)
pdf.cell(0, 20, text="Invoice", new_x="LMARGIN", new_y="NEXT", align="C")

# Subtitle / info
pdf.set_font("helvetica", size=12)
pdf.cell(0, 10, text="Customer: John Doe", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 10, text="Date: 31-Oct-2025", new_x="LMARGIN", new_y="NEXT")

# Table header
pdf.set_font("helvetica", "B", 12)
pdf.cell(80, 10, text="Item", border=1)
pdf.cell(30, 10, text="Qty", border=1)
pdf.cell(30, 10, text="Price", border=1)
pdf.cell(30, 10, text="Total", border=1, new_x="LMARGIN", new_y="NEXT")

# Table body
pdf.set_font("helvetica", size=12)
grand_total = 0

for row in report_data:
    total = row["qty"] * row["price"]
    grand_total += total
    pdf.cell(80, 10, text=row["item"], border=1)
    pdf.cell(30, 10, text=str(row["qty"]), border=1)
    pdf.cell(30, 10, text=f"${row['price']:.2f}", border=1)
    pdf.cell(30, 10, text=f"${total:.2f}", border=1, new_x="LMARGIN", new_y="NEXT")

# Grand total
pdf.set_font("helvetica", "B", 12)
pdf.cell(140, 10, text="Grand Total", border=1)
pdf.cell(30, 10, text=f"${grand_total:.2f}", border=1, new_x="LMARGIN", new_y="NEXT")

# Save PDF
pdf.output(pdf_output)
