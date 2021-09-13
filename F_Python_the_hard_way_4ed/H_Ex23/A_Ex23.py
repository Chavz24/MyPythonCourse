import sys

encoding = sys.argv[1]
error = sys.argv[2]


def main(lan_file, encoding, errors):
    line = lan_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(lan_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    try:
        raw_bytes = next_lang.encode(encoding, errors=errors)
        cooked_string = raw_bytes.decode(encoding, errors=errors)
        print(raw_bytes)
    except UnicodeEncodeError:
        pass



with open("lan.txt", mode="r", encoding="utf-8") as file:
    main(file, encoding, error)
