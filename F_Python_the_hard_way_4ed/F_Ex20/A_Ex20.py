from sys import argv

file_name = argv[1]


def print_all(file):
    """This function prints all the lines in a file"""

    print(file.read())


def rewind(file):
    """This function moves the 'read head' to the start of the file"""

    print(file.seek(0))


def print_a_line(current_line, file):
    """This function reads the file one live at the time"""

    print(current_line, file.readline(),end='')


with open(file_name, mode="r") as input_file:
    print("Printing the whole file...")
    print_all(input_file)
    print("Moving to the first line...")
    rewind(input_file)
    line_num = 1
    print("Printing one line at the time...")
    print_a_line(line_num, input_file)
    line_num += 1
    print_a_line(line_num, input_file)
    line_num += 1
    print_a_line(line_num, input_file)
