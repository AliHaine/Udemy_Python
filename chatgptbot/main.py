import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QToolBar, QStatusBar,
							QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QTextEdit)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import openai
from openai import OpenAIError


class ChatBotWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setMinimumSize(750, 500)

		self.chat_area = QTextEdit(self)
		self.chat_area.setReadOnly(True)
		self.chat_area.setGeometry(10, 10, 480, 320)

		self.input_field = QLineEdit(self)
		self.input_field.setGeometry(10, 340, 480, 40)

		self.button = QPushButton("Send", self)
		self.button.setGeometry(500, 340, 80, 40)
		self.button.clicked.connect(self.run_chat)

		self.show()

	def run_chat(self):
		response = bot.get_response(self.input_field.text())
		self.chat_area.append(f"Me: {self.input_field.text()}")

		self.chat_area.append(f"Chat: {response}")


class ChatBot:
	def __init__(self):
		pass

	def get_response(self, user_input):
		try:
			response = openai.chat.completions.create(
				model="gpt-3.5-turbo",
				messages=[
					{"role": "system", "content": "You are a helpful assistant."},
					{"role": "user", "content": user_input}
				],
				max_tokens=50,
			).choices[0].text
		except OpenAIError as e:
			print(e)
			response = "null"
		return response


bot = ChatBot()
app = QApplication(sys.argv)
main_win = ChatBotWindow()
sys.exit(app.exec())
