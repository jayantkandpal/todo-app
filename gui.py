from helper import todoFunctions
import FreeSimpleGUI as sg
import time

sg.theme('BlueMono')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button(tooltip="Click to add todo", button_text="Add", size=10)
complete_button = sg.Button(tooltip="Click to mark todo as complete", button_text="Complete", size=10)
exit_button = sg.Button(tooltip="Click to exit todos app", button_text="Exit", size=10)

list_box = sg.Listbox(values=todoFunctions.get_todos(), enable_events=True,
                      key="todos", size=[45,10])
edit_button = sg.Button(tooltip="Click to edit todo", button_text="Edit", size=10)

window = sg.Window('TODO app',
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box,[edit_button,complete_button]],
                       [exit_button]
                   ],
                   font=("Helvetica", 14))

while True:
    event, values = window.read(timeout=200)
    match event:
        case "Add":
            todos = todoFunctions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            todoFunctions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = todoFunctions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                todoFunctions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 14))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = todoFunctions.get_todos()
                todos.remove(todo_to_complete)
                todoFunctions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 14))
        case "Exit":
            break
        case 'todos':
            window["todo"].update(value=values['todos'][0].strip())
        case sg.WIN_CLOSED:
            break
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    window['clock'].update(value=time.strftime("%Y-%m-%d %H:%M:%S") )

window.close()