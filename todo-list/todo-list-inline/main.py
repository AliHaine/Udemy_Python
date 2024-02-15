file = open("todo.txt", 'r+')
todos = file.read().splitlines()


def get_int_from_txt(txt):
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
    if "show" in user_action or "display" in user_action:
        show_action()
    elif "add" in user_action:
        todos.append(user_action.removeprefix("add "))
    elif "edit" in user_action:
        show_action()
        try:
            val = get_int_from_txt(user_action[user_action.find(' '):])
        except ValueError:
            print("This is not a number or the number is too large")
            continue
        todos[val] = input("Enter the new value for " + str(val) + "\n")
    elif "complete" in user_action:
        show_action()
        try:
            val = get_int_from_txt(user_action[user_action.find(' '):])
        except ValueError:
            print("This is not a number or the number is too large")
            continue
        todos.pop(val)
    elif "exit" in user_action:
        break
    else:
        print("Try again")
    write_to_file()

file.close()
