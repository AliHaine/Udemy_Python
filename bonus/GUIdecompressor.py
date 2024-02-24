import PySimpleGUI as sg
import shutil_browser_test

label1 = sg.Text("Select archive")
input1 = sg.Input()
choose1 = sg.FileBrowse("CHOOSE", key="archive")

label2 = sg.Text("Destin folder")
input2 = sg.Input()
choose2 = sg.FolderBrowse("CHOOSE", key="folder")

confirm = sg.Button("enter")

win = sg.Window("", [[label1, input1, choose1], [label2, input2, choose2], [confirm]])

while True:
	event, values = win.read()
	filepath = values["archive"]
	dest = values["folder"]
	shutil_browser_test.decompress_archive(filepath, dest)

win.close()