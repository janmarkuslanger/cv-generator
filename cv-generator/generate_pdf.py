from fpdf import FPDF
from data import DataSource


def generate_pdf(data: DataSource) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, text="Hello, FPDF!", ln=True, align='C')
    pdf.output("cv.pdf")