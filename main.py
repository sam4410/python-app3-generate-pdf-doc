from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')
# print(type(pdf))

for idx, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    for y in range(20, 298, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    pdf.ln(265)   # adding 278 break lines
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    # adding subsequent blank pages
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(277)  # adding 278 break lines
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

        for y in range(20, 298, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

pdf.output("output.pdf")
