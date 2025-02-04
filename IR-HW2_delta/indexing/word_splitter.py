import os
import re

from nltk import SnowballStemmer

stopwords = open(os.path.dirname(__file__)+"/nltk-stopwords.txt").read().split("\n")

stemmer = SnowballStemmer('english')





#it has all the correct positions of the words in the original
def get_words(text,x):
    words = x.findall(text)
    words = map(lambda x: x.strip().strip("_").lower(), words)
    words = filter(lambda x: x != 's' and x != '', words)  # removes all apostrophes
    words = list(words)
    return words


def get_words_splitting(text):
    arr = text.strip().replace('-', ' ').split()
    words = list(map(lambda val: val.strip().strip("_,.\"()<>``''").lower(), arr))
    words = filter(lambda x: x != 's' and x != '', words)  # removes all apostrophes
    return words


# words = get_words("""U.S. Attorney for the District of Columbia Jay B. Stephens, who
# can prosecute both local and federal crimes""")
#
# print(words)
#
# stemmed_not_stopped = list(map(lambda x: stemmer.stem(x), words))
# filtered_stop = list(filter(lambda x: x not in stopwords, words))
# stemmed_stopped = list(map(lambda x: stemmer.stem(x), filtered_stop))
#
# print(stemmed_stopped)
