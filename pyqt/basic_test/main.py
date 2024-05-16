from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime


class AgeCalculator(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")
		grid = QGridLayout()

		name_label = QLabel("Name")
		self.name_line_edit = QLineEdit()

		birth_label = QLabel("Birth MM/DD/YYYY")
		self.birth_line_edit = QLineEdit()

		calculate_button = QPushButton()
		calculate_button.clicked.connect(self.calculate_age)
		self.output_label = QLabel("")

		grid.addWidget(name_label, 0, 0)
		grid.addWidget(self.name_line_edit, 0, 1)
		grid.addWidget(birth_label, 1, 0)
		grid.addWidget(self.birth_line_edit, 1, 1)
		grid.addWidget(calculate_button, 2, 0, 1, 2)
		grid.addWidget(self.output_label, 3, 0, 1, 2)

		self.setLayout(grid)

	def calculate_age(self):
		cur_date = datetime.now().year
		user_date = self.birth_line_edit.text()
		user_year_date = datetime.strptime(user_date, "%m/%d/%Y").date().year
		age = cur_date - user_year_date
		self.output_label.setText(f"{self.name_line_edit.text()}  {age}")


app = QApplication(sys.argv)
ac = AgeCalculator()
ac.show()
sys.exit(app.exec())