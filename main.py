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

    with open(filepath, "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")
