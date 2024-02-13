file = open("todo.txt", 'r+')
todos = file.read().splitlines()

def get_int_from_input(txt):
    val = int(input(txt))
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
    match user_action:
        case "show" | "display":
            show_action()
        case "add":
            todos.append(input("Text to add:\n"))
        case "edit":
            show_action()
            try:
                val = get_int_from_input("Which one you want to edit\n")
            except ValueError:
                print("This is not a number or the number is too large")
                continue
            todos[val] = input("Enter the new value for " + str(val) + "\n")
        case "complete":
            show_action()
            try:
                val = get_int_from_input("Which one you have completed\n")
            except ValueError:
                print("This is not a number or the number is too large")
                continue
            todos.pop(val)
        case "exit":
            break
        case _:
            print("Try again")
    write_to_file()

file.close()
