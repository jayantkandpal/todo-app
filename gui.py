from helper import todoFunctions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(tooltip="Click to add todo", button_text="Add")
edit_button = sg.Button(tooltip="Click to edit todo", button_text="Edit")
complete_button = sg.Button(tooltip="Click to mark todo as complete", button_text="Complete")
show_button = sg.Button(tooltip="Click to view all todos", button_text="Show")

window = sg.Window('TODO app',
                   layout=[
                       [label,input_box],
                       [add_button, edit_button, complete_button, show_button]
                   ],
                   font=("Helvetica", 16))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = todoFunctions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            todoFunctions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()