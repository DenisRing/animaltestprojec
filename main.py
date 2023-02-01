import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("animals/*txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdftitle = Path(filepath).stem
    name = pdftitle.title()
    #pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell( w=50, h=8, txt=name)
    #pdf.output(f"PDFs/{pdftitle}.pdf")

pdf.output("output.pdf")
