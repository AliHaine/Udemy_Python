from fpdf import FPDF
import pandas


def set_footer(footer, ln):
	pdf.ln(ln)
	pdf.set_font(family="Times", size=8, style="I")
	pdf.cell(w=0, h=8, txt=footer, ln=1, align="R")


def create_page_and_topic(topic):
	pdf.add_page()
	pdf.set_font(family="Times", size=21)
	pdf.cell(w=0, h=12, txt=topic, ln=1)
	pdf.line(10, 21, 200,21)
	set_footer(topic, 246)


pdf = FPDF(orientation="P", unit="mm", format="A4")
listData = pandas.read_csv("data.csv", delimiter=",")

for index, iterator in listData.iterrows():
	create_page_and_topic(iterator["Topic"])
	for i in range(iterator["Pages"] - 1):
		pdf.add_page()
		set_footer(iterator["Topic"], 256)

pdf.output("test.pdf")
