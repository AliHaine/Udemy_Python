import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype={"id": str})

class Article:
	def __init__(self, article_rows):
		self.article_id = article_rows["id"].values[0]
		self.article_name = article_rows["name"].values[0]
		self.article_price = article_rows["price"].values[0]
		self.article_stock = article_rows["in stock"].values[0]

	def create_pdf(self):
		pdf = FPDF(orientation="P", unit="mm", format="A4")
		pdf.add_page()
		pdf.set_font(family="Times", size=16, style="B")

		pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article_id}", ln=1)
		pdf.cell(w=50, h=8, txt=f"Article: {self.article_name}", ln=1)
		pdf.cell(w=50, h=8, txt=f"Price: {self.article_price}", ln=1)

		pdf.output("receipt.pdf")

	def executor(self):
		self.create_pdf()
		df.loc[df["id"] == self.article_id, "in stock"] = self.article_stock - 1
		df.to_csv("articles.csv", index=False)


print(df)
value = input("Select article\n")
article_rows = df.loc[df["id"] == value]
article = Article(article_rows)
article.executor()
