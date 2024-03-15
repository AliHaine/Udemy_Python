import pandas
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
square = (20,50,75)


def get_width(txt):
	w = pdf.get_string_width(str(txt)) + 2
	if w < 20:
		w = square[0]
	elif w <= 50:
		w = square[1]
	else:
		w = square[2]
	return w


def test2(values):
	for val in values:
		pdf.cell(w=get_width(val), h=12, txt=str(val), border=1)
	pdf.ln()


def test(value):
	pdf.cell(w=get_width(value), h=12, txt=str(value), border=1)


data = pandas.read_excel("10001-2023.1.18.xlsx")
pdf.add_page()
pdf.set_font(family="Times", size=12)

test2(("Id", "Product name", "Number", "Price", "Total"))
for a, b in data.iterrows():
	b.apply(test)
	pdf.ln()
test2(("", "                     ", "", "", data["total_price"].sum()))


pdf.output("result.pdf")
