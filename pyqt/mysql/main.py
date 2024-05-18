from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QToolBar, QStatusBar,
							QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import sys
import sqlite3
import mysql.connector


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Class management")
		self.setMinimumSize(400, 500)

		file_menu_item = self.menuBar().addMenu("Test")
		help_menu_item = self.menuBar().addMenu("Help")
		edit_menu_item = self.menuBar().addMenu("Edit")

		add_student_action = QAction("Add student", self)
		add_student_action.triggered.connect(self.add_action)
		file_menu_item.addAction(add_student_action)

		about_action = QAction("About", self)
		help_menu_item.addAction(about_action)

		search_action = QAction("Search", self)
		search_action.triggered.connect(self.search_action)
		edit_menu_item.addAction(search_action)

		self.table = QTableWidget()
		self.table.setColumnCount(4)
		self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
		self.table.verticalHeader().setVisible(False)
		self.setCentralWidget(self.table)
		self.load_data()

		toolbar = QToolBar()
		toolbar.setMovable(True)
		self.addToolBar(toolbar)
		toolbar.addAction(add_student_action)
		toolbar.addAction(search_action)

		self.statusbar = QStatusBar()
		self.setStatusBar(self.statusbar)

		self.table.cellClicked.connect(self.cell_clicked)



	def load_data(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM students")
		result = cursor.fetchall()
		self.table.setRowCount(0)
		for row_number, row_data in enumerate(result):
			self.table.insertRow(row_number)
			for col_number, col_data in enumerate(row_data):
				self.table.setItem(row_number, col_number, QTableWidgetItem(str(col_data)))
		cursor.close()

	def add_action(self):
		dialog = InsertDialog()
		dialog.exec()

	def search_action(self):
		dialog = SearchDialog()
		dialog.exec()

	def edit_action(self):
		edit = editDialog()
		edit.exec()

	def delete_action(self):
		selected_index = main_win.table.currentRow()

		cursor = connection.cursor()
		cursor.execute("DELETE FROM students WHERE id = %s", (main_win.table.item(selected_index, 0).text(), ))
		connection.commit()
		cursor.close()
		main_win.load_data()

	def cell_clicked(self):
		edit_button = QPushButton("Edit")
		edit_button.clicked.connect(self.edit_action)
		delete_button = QPushButton("Delete")
		delete_button.clicked.connect(self.delete_action)

		children = self.findChildren(QPushButton)
		if (children):
			for child in children:
				self.statusbar.removeWidget(child)

		self.statusbar.addWidget(edit_button)
		self.statusbar.addWidget(delete_button)


class InsertDialog(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Insert student")
		self.setFixedWidth(450)
		self.setFixedHeight(450)

		layout = QVBoxLayout()

		self.student_name = QLineEdit()
		self.student_name.setPlaceholderText("Name")
		layout.addWidget(self.student_name)

		self.course_name = QComboBox()
		courses = ["Bio", "Math", "Info"]
		self.course_name.addItems(courses)
		layout.addWidget(self.course_name)


		self.mobile_name = QLineEdit()
		self.mobile_name.setPlaceholderText("Mobile")
		layout.addWidget(self.mobile_name)

		button = QPushButton("Register")
		button.clicked.connect(self.add_student)
		layout.addWidget(button)

		self.setLayout(layout)

	def add_student(self):
		name = self.student_name.text()
		course = self.course_name.currentText()
		mobile = self.mobile_name.text()
		cursor = connection.cursor()
		cursor.execute("INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)", (name, course, mobile))
		connection.commit()
		cursor.close()
		main_win.load_data()


class SearchDialog(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Serach student")
		self.setFixedWidth(450)
		self.setFixedHeight(450)

		layout = QVBoxLayout()

		self.student_name = QLineEdit()
		self.student_name.setPlaceholderText("Name")
		layout.addWidget(self.student_name)

		button = QPushButton("Search")
		button.clicked.connect(self.search_student)
		layout.addWidget(button)

		self.setLayout(layout)

	def search_student(self):
		connection = sqlite3.connect("database.db")
		cursor = connection.cursor()
		cursor.execute(f"SELECT * FROM students WHERE name='{self.student_name.text()}'")
		result = cursor.fetchall()
		items = main_win.table.findItems(self.student_name.text(), Qt.MatchFlag.MatchFixedString)
		for item in items:
			print(item)
			main_win.table.item(item.row(), 1).setSelected(True)

		cursor.close()
		connection.close()


class editDialog(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Edit student")
		self.setFixedWidth(450)
		self.setFixedHeight(450)

		selected_index = main_win.table.currentRow()

		layout = QVBoxLayout()

		self.student_name = QLineEdit(main_win.table.item(selected_index, 1).text())
		layout.addWidget(self.student_name)

		self.student_id = main_win.table.item(selected_index, 0).text()

		self.course_name = QComboBox()
		courses = ["Bio", "Math", "Info"]
		self.course_name.addItems(courses)
		self.course_name.setCurrentText(main_win.table.item(selected_index, 2).text())
		layout.addWidget(self.course_name)

		self.mobile_name = QLineEdit(main_win.table.item(selected_index, 3).text())
		layout.addWidget(self.mobile_name)

		button = QPushButton("Edit")
		button.clicked.connect(self.update_student)
		layout.addWidget(button)

		self.setLayout(layout)

	def update_student(self):
		cursor = connection.cursor()
		cursor.execute("UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s",
					(self.student_name.text(), self.course_name.currentText(), self.mobile_name.text(), self.student_id))
		connection.commit()
		cursor.close()
		main_win.load_data()
		self.window().close()


connection = mysql.connector.connect(host="localhost", user="root", password="pythoncourse", database="test")
app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
exec_code = app.exec()
connection.close()
sys.exit(exec_code)
