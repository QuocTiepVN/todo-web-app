def get_todo():
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg):
    with open("todos.txt", "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todo())