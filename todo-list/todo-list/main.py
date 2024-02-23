import function

while True:
    user_action = input("Enter action:\n").strip().lower()
    if user_action.startswith("show") or user_action.startswith("display"):
        function.show_action()
    elif user_action.startswith("add"):
        function.write_to_todos_list(user_action.removeprefix("add "))
    elif user_action.startswith("edit"):
        function.show_action()
        try:
            val = function.get_int_from_txt(user_action[user_action.find(' '):])
        except ValueError:
            print("This is not a number or the number is too large")
            continue
        function.edit_action(val, input("Enter the new value for " + str(val) + "\n"))
    elif user_action.startswith("complete"):
        function.show_action()
        try:
            val = function.get_int_from_txt(user_action[user_action.find(' '):])
        except ValueError:
            print("This is not a number or the number is too large")
            continue
        function.remove_from_todos_list(val)
    elif user_action.startswith("exit"):
        break
    else:
        print("Try again")
    function.write_to_file()
function.close_file()
