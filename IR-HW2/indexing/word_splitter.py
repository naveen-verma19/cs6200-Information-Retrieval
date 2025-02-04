import re


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def word_filter(word):
    val1 = word != ""
    val2 = len(word) > 1 or (len(word) == 1 and RepresentsInt(word))
    return val1 and val2


def get_words(text):
    words = re.findall(r'(?:(?:\$)\d*(?:[.,](?:\d)+)*)|(?:\w*(?:\.(?:\w)+)*)', text)
    words = list(map(lambda val: val.strip().strip("_,.\"()<>``''").lower(), words))
    words = list(filter(lambda val: word_filter(val), words))

    # DEBUG AND REMOVE MORE WORDS LATER
    return words


def get_words_splitting(text):
    arr = text.strip().replace('-', ' ').split()
    words = list(map(lambda val: val.strip().strip("_,.\"()<>``''").lower(), arr))
    words = list(filter(lambda val: word_filter(val), words))
    return words
