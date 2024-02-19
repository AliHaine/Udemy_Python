file = open("todo.txt", 'r+')
todos = file.read().splitlines()


def get_int_from_txt(txt):
    """Convert str to int"""
    val = int(txt)
    if val > len(todos) - 1 or val < 0:
        raise ValueError
    return val


def show_action():
    for index, txt in enumerate(todos):
        print(f"{index}-{txt}")


def write_to_file():
    file.seek(0)
    for txt in todos:
        file.writelines(txt + "\n")


while True:
    user_action = input("Enter action:\n").strip().lower()
    if user_action.startswith("show") or user_action.startswith("display"):
        show_action()
    elif user_action.startswith("add"):
        todos.append(user_action.removeprefix("add "))
    elif user_action.startswith("edit"):
        show_action()
        try:
            val = get_int_from_txt(user_action[user_action.find(' '):])
        except ValueError:
            print("This is not a number or the number is too large")
            continue
        todos[val] = input("Enter the new value for " + str(val) + "\n")
    elif user_action.startswith("complete"):
        show_action()
        try:
            val = get_int_from_txt(user_action[user_action.find(' '):])
        except ValueError:
            print("This is not a number or the number is too large")
            continue
        todos.pop(val)
    elif user_action.startswith("exit"):
        break
    else:
        print("Try again")
    write_to_file()

file.close()
