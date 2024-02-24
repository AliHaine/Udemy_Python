import function
import PySimpleGUI as sg
import time

clock = sg.Text('', key='clock')
label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter text", key="input_box")
list_box = sg.Listbox(values=function.get_todos_list(), size=(45, 10), key="list_box")
edit_button = sg.Button("Edit")
#add_button = sg.Button(image_source='vivre.png', key="Add")
add_button = sg.Button("Add", key="Add")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")


win = sg.Window("Todo",
				layout=[[clock], [label, input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
				font=('Helvetica', 15))

while True:
	event, value = win.read(timeout=90)
	match event:
		case "Add":
			function.write_to_todos_list(value['input_box'])
		case "Edit":
			try:
				function.edit_action(function.get_index_of(value["list_box"][0]), value["input_box"])
			except IndexError:
				sg.popup_error("Please select a item first", auto_close=True, auto_close_duration=2)
		case "Complete":
			function.remove_from_todos_list(function.get_index_of(value["list_box"][0]))
		case "Exit" | sg.WIN_CLOSED:
			break
	win['list_box'].update(values=function.get_todos_list())
	win['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
	function.write_to_file()

win.close()
