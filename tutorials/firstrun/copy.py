
def copy(file_name, new_file_name):
    contents = ""
    with open(file_name) as file:
        contents = file.read()

    with open(new_file_name, 'w') as file:
        file.write(contents)

def copy_and_reverse(file_name, new_file_name):
    contents = ""
    with open(file_name) as file:
        contents = file.read()

    with open(new_file_name, 'w') as file:
        file.write(contents)