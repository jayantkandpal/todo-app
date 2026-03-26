from src.helper import todoFunctions
import time

now = time.strftime("%Y-%m-%d %H:%M:%S")
print("Welcome to the todo list")
print("Time: ", now)

while True:
    user_action = input("Enter command: add, edit, show, complete or exit - ")

    if user_action.startswith("add"):
        # list slicing:
        newTodo = user_action[4:] + '\n'
        with open(r'../resources/todos.txt', 'a') as file:
            file.write(newTodo)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = todoFunctions.get_todos()
            new_todo = input('Enter new todo: ') + '\n'
            todos.__setitem__(number, new_todo)
            print("Todo updated to: ", new_todo.strip('\n'))

            todoFunctions.write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue
        except IndexError:
            print("There is no todo item with that number to edit!")
            continue

    elif user_action.startswith("show"):
        todos = todoFunctions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index+1}. {item.strip('\n')}")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = todoFunctions.get_todos()
            print("TODO completed: ", todos.pop(number - 1).strip('\n'))

            todoFunctions.write_todos(todos)
        except IndexError:
            print("There is no todo item with that number to mark complete!")
            continue

    elif user_action.startswith("exit "):
        break

    else:
        print("Invalid command!")

print("Bye bye!")


