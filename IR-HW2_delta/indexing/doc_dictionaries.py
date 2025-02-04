import os
import re

import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize.api import TokenizerI
from sortedcontainers import SortedSet

from indexing.word_splitter import get_words

stemmer = SnowballStemmer('english')

stopwords = set(open(os.path.dirname(__file__)+"/nltk-stopwords.txt").read().split("\n"))

#
# def get_token_elasticsearch(text):
#     es = connect_elasticsearch()
#     cl = IndicesClient(es)
#     res = cl.analyze(index="ap89", body={
#         "analyzer": "my_analyzer",
#         "text": text
#     })
#     return list(map(lambda t: t["token"], res["tokens"]))

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def two_digit_filter(word):
    if len(word) > 2:
        return True
    if len(word) == 2:
        if RepresentsInt(word) or word == "u.":
            return True
    return False

# Finds all 1 based indices for word in words
# "sam" in "sam is sam" =[1,3]
def find_all(words, word):
    indices = [i + 1 for i, x in enumerate(words) if x == word]
    return indices


def get_dict_stopped_not_stemmed(text, x):
    words = get_words(text, x)
    doc1_dict_stopped = {}

    for i, word in enumerate(words):
        if (word not in stopwords) and two_digit_filter(word):
            if word not in doc1_dict_stopped.keys():
                doc1_dict_stopped[word] = [i + 1]
            else:
                doc1_dict_stopped[word].append(i + 1)
    return doc1_dict_stopped



def get_dict_stopped_stemmed(text, x):
    words = get_words(text, x)
    doc1_dict_stopped = {}

    for i, word in enumerate(words):
        if (word not in stopwords) and two_digit_filter(word):
            stemmed = stemmer.stem(word)
            if stemmed not in doc1_dict_stopped.keys():
                doc1_dict_stopped[stemmed] = [i + 1]
            else:
                doc1_dict_stopped[stemmed].append(i + 1)
    return doc1_dict_stopped


# doc_text = """98.6 For AVA'S aunt's _ags _shh 12 ab re sr students working student in a miniature factory at
# the University of Missouri-Rolla, Universities student work the future of American business is
# now. students The celluloid torch has been passed to a new $123,23442 344, 564 12.232 1.2 12.22 1,222 12,2222 12, 22
# 4.4.5.5.5. 1222,333,444 aunt's u.s iran-contra d'etat b123 I.I.T sab.ss
# generation: filmmakers who grew up in the 1960s aunt's a.sd s _a.
#    ``Platoon,'' ``Running on Empty,'' ``1969'' and ``Mississippi"""
#
# x = re.compile(r'(?:\d+(?:[.,]\d+)*)|(?:\w+(?:\.(?:\w)+)*)')
# words = x.findall(doc_text)
# words = map(lambda x: x.strip().strip("_").lower(), words)
# words = filter(lambda x: x != 's' and x != '', words)  # removes all apostrophes
# words=list(words)
# print(doc_text.split())
# print(len(words))
# print(words)
# start = time()
# print(get_dict_stopped_not_stemmed(doc_text,x))
# print(get_dict_stopped_not_stemmed(doc_text, x))
# print(get_dict_stopped_stemmed(doc_text, x))
# print(get_dict_stopped_stemmed(doc_text, x))
# print(get_dict_stopped_stemmed(doc_text, x))
# print(get_dict_stopped_stemmed(doc_text, x))
# print(get_dict_stopped_stemmed(doc_text, x))
# print(time() - start)
