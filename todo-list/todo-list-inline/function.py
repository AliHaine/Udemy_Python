def get_int_from_txt(txt, todos):
    """Convert str to int"""
    val = int(txt)
    if val > len(todos) - 1 or val < 0:
        raise ValueError
    return val


def show_action(todos):
    for index, txt in enumerate(todos, todos):
        print(f"{index}-{txt}")


def write_to_file(file, todos):
    file.seek(0)
    for txt in todos:
        file.writelines(txt + "\n")