import sys

encoding = sys.argv[1]
error = sys.argv[2]


def main(lan_file, encoding, errors):
    line = lan_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(lan_file, encoding, errors)


def print_line(line, encoding, errors):
    raw_bytes=line.strip()

    #raw_bytes = next_lang.encode(encoding, errors=errors)
    #cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes.decode())




with open("bytes.txt", mode="rb") as file:
    main(file, encoding, error)


