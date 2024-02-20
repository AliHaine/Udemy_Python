import function

file = open("todo.txt", 'r+')
todos = file.read().splitlines()


while True:
    user_action = input("Enter action:\n").strip().lower()
    if user_action.startswith("show") or user_action.startswith("display"):
        function.show_action(todos)
    elif user_action.startswith("add"):
        todos.append(user_action.removeprefix("add "))
    elif user_action.startswith("edit"):
        function.show_action(todos)
        try:
            val = function.get_int_from_txt(user_action[user_action.find(' '):], todos)
        except ValueError:
            print("This is not a number or the number is too large")
            continue
        todos[val] = input("Enter the new value for " + str(val) + "\n")
    elif user_action.startswith("complete"):
        function.show_action(todos)
        try:
            val = function.get_int_from_txt(user_action[user_action.find(' '):], todos)
        except ValueError:
            print("This is not a number or the number is too large")
            continue
        todos.pop(val)
    elif user_action.startswith("exit"):
        break
    else:
        print("Try again")
    function.write_to_file(file, todos)

file.close()
