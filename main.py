import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("animals/*txt")

for filepath in filepaths:
    pdftitle = Path(filepath).stem
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell( w=50, h=8, txt=pdftitle.title())
    pdf.output(f"PDFs/{pdftitle}.pdf")
