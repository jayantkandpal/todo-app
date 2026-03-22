from helper import todoFunctions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button(tooltip="Click to add todo", button_text="Add")
complete_button = sg.Button(tooltip="Click to mark todo as complete", button_text="Complete")
show_button = sg.Button(tooltip="Click to view all todos", button_text="Show")

list_box = sg.Listbox(values=todoFunctions.get_todos(), enable_events=True,
                      key="todos", size=[45,10])
edit_button = sg.Button(tooltip="Click to edit todo", button_text="Edit")

window = sg.Window('TODO app',
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box,edit_button]
                   ],
                   font=("Helvetica", 16))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = todoFunctions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            todoFunctions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = todoFunctions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            todoFunctions.write_todos(todos)
            window["todos"].update(values=todos)
        case 'todos':
            window["todo"].update(value=values['todos'][0].strip())
        case sg.WIN_CLOSED:
            break

window.close()