def break_sentence(sentence):
    """This function breaks a sentence in to words"""

    words = sentence.split(" ")
    return words


def sort_words(words):
    """This function sorts all the words"""

    return sorted(words)


def print_first_word(words):
    """This function returns the first word in a list"""

    word = words.pop(0)
    print(word)


def print_last_word(words):
    """This function returns the last word in a list"""

    word = words.pop(-1)
    print (word)


def sort_sentence(sentence):
    """This function takes a full sentence and returns the sorted words"""

    words = break_sentence(sentence)
    return sort_words(words)


def print_first_last(sentence):
    """This function returns the first and last words of a sentence"""

    words = break_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""

    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
