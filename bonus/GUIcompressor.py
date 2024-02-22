import PySimpleGUI as sg

label1 = sg.Text("Select file")
input1 = sg.Input()
choose1 = sg.FileBrowse("CHOOSE")

label2 = sg.Text("Destin file")
input2 = sg.Input()
choose2 = sg.FileBrowse("CHOOSE")

confirm = sg.Button("enter")

win = sg.Window("", [[label1, input1, choose1], [label2, input2, choose2], [confirm]])

win.read()