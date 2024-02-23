import function
import PySimpleGUI as sg

label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter text", key="input_box")
list_box = sg.Listbox(values=function.get_todos_list(), size=(45, 10), key="list_box")
edit_button = sg.Button("Edit")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")


win = sg.Window("Todo",
				layout=[[label, input_box, add_button], [list_box, edit_button], [exit_button]],
				font=('Helvetica', 20))

while True:
	event, value = win.read()
	match event:
		case "Add":
			function.write_to_todos_list(value['input_box'])
		case "Edit":
			function.edit_action(function.get_index_of(value["list_box"][0]), value["input_box"])
		case "Exit" | sg.WIN_CLOSED:
			break
	win['list_box'].update(values=function.get_todos_list())
	function.write_to_file()

win.close()
