FILEPATH = "resources/todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of todos
    :param filepath:
    :return:
    """
    # with-context manager:
    with open(filepath, "r") as todos_file:
        todos_in_file = todos_file.readlines()
    return todos_in_file

def write_todos(todos_to_write, filepath=FILEPATH):
    """
    Write a list of todos to a text file
    :param todo_to_write:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as write_file:
        write_file.writelines(todos_to_write)

if __name__ == "__main__":
    print("Hello from todo functions py file")
