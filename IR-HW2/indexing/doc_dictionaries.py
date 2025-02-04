from elasticsearch import Elasticsearch
from nltk.stem.snowball import SnowballStemmer

from indexing.word_splitter import get_words
from elasticsearch.client import IndicesClient


stemmer = SnowballStemmer('english')

stopwords = open("nltk-stopwords.txt").read().split("\n")

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    return _es


def get_token_elasticsearch(text):
    es = connect_elasticsearch()
    cl = IndicesClient(es)
    res = cl.analyze(index="ap89", body={
        "analyzer": "my_analyzer",
        "text": text
    })
    return list(map(lambda t:t["token"], res["tokens"]))


# Finds all 1 based indices for word in words
# "sam" in "sam is sam" =[1,3]
def find_all(words, word):
    indices = [i + 1 for i, x in enumerate(words) if x == word]
    return indices


def get_dict_stopped_not_stemmed(text):
    words= get_words(text)

    filtered_stop = list(filter(lambda x: x not in stopwords, words))
    doc1_dict_stopped_not_stemmed = {}
    for word in filtered_stop:
        if word not in doc1_dict_stopped_not_stemmed.keys():
            doc1_dict_stopped_not_stemmed[word] = find_all(words, word)
    return doc1_dict_stopped_not_stemmed


def get_dict_stopped_stemmed(text):
    words= get_words(text)
    stemmed_not_stopped = list(map(lambda x: stemmer.stem(x), words))
    filtered_stop = list(filter(lambda x: x not in stopwords, words))
    stemmed_stopped = list(map(lambda x: stemmer.stem(x), filtered_stop))
    # stemmed_stopped=get_token_elasticsearch(text)
    doc1_dict_stopped_stemmed = {}
    for stemmed_word in stemmed_stopped:
        if stemmed_word not in doc1_dict_stopped_stemmed.keys():
            doc1_dict_stopped_stemmed[stemmed_word] = find_all(stemmed_not_stopped, stemmed_word)
    return doc1_dict_stopped_stemmed


doc_text = """98.6 For students working student in a miniature factory at
the University of Missouri-Rolla, Universities work the future of American business is
now. students"""
