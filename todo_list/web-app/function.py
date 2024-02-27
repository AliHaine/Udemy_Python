import os

file_name = "data.csv"

if not (os.path.exists(file_name)):
    with open(file_name, 'w') as f:
        pass


file = open(file_name, 'r+')
todos = file.read().splitlines()
file.close()


def get_int_from_txt(txt):
    """Convert str to int"""
    val = int(txt)
    if val > len(todos) - 1 or val < 0:
        raise ValueError
    return val


def show_action():
    for index, txt in enumerate(todos):
        print(f"{index}-{txt}")


def edit_action(val, txt):
    todos[val] = txt


def write_to_file():
    file = open(file_name, 'w')
    for txt in todos:
        file.writelines(txt + "\n")


def write_to_todos_list(txt):
    todos.append(txt)


def remove_from_todos_list(val):
    todos.pop(val)


def close_file():
    file.close()


def get_todos_list():
    return todos


def get_index_of(txt):
    return todos.index(txt)


if __name__ == "__main__":
    print("main")
