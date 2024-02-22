import function
import PySimpleGUI as sg

label = sg.Text("test")
input_box = sg.InputText(tooltip="Enter text")
button = sg.Button("add")


win = sg.Window("title", layout=[[label, input_box], [sg.Text("oui"), button]])
read = win.read()
print(read)
