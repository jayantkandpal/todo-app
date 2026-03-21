from helper import todoFunctions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button(tooltip="Click to add todo", button_text="Add todo")
edit_button = sg.Button(tooltip="Click to edit todo", button_text="Edit todo")
complete_button = sg.Button(tooltip="Click to mark todo as complete", button_text="Complete todo")
show_button = sg.Button(tooltip="Click to view all todos", button_text="Show todos")

window = sg.Window('TODO app',
                   layout=[[label,input_box],[add_button,edit_button,complete_button,show_button]])
window.read()

window.close()