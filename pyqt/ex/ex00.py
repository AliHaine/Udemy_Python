from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys


class CalcDistance(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")
		grid = QGridLayout()

		dist_label = QLabel("Distance")
		self.dist_line_edit = QLineEdit()

		time_label = QLabel("Time (hour)")
		self.time_line_edit = QLineEdit()

		cal_button = QPushButton("Calculate")
		cal_button.clicked.connect(self.calc_distance)
		self.output_label = QLabel("")

		self.comboBox = QComboBox(self)
		self.comboBox.addItem("Metric (km)")
		self.comboBox.addItem("Imperial (milles)")

		grid.addWidget(dist_label, 0, 0)
		grid.addWidget(self.dist_line_edit, 0, 1)
		grid.addWidget(self.comboBox, 0, 3)
		grid.addWidget(time_label, 1, 0)
		grid.addWidget(self.time_line_edit, 1, 1)
		grid.addWidget(cal_button, 2, 1)
		grid.addWidget(self.output_label, 3, 1)

		self.setLayout(grid)

	def calc_distance(self):
		self.output_label.setText(str(int(self.dist_line_edit.text()) / int(self.time_line_edit.text())))




app = QApplication(sys.argv)
cd = CalcDistance()
cd.show()
sys.exit(app.exec())