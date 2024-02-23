import PySimpleGUI as sg
from shutil_browser_test import make_archive

label1 = sg.Text("Select file")
input1 = sg.Input()
choose1 = sg.FileBrowse("CHOOSE", key="files")

label2 = sg.Text("Destin file")
input2 = sg.Input()
choose2 = sg.FolderBrowse("CHOOSE", key="folder")

confirm = sg.Button("enter")

win = sg.Window("", [[label1, input1, choose1], [label2, input2, choose2], [confirm]])

while True:
	event, values = win.read()
	filepath = values["files"]
	dest = values["folder"]
	make_archive(filepath, dest)

win.close()