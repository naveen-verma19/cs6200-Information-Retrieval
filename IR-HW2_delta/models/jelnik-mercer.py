import collections
import json
import math
import re

from nltk.stem.snowball import SnowballStemmer

from models.index_constants import get_average_doc_length, get_total_documents, get_vocab_size
from test_indexing import get_all_docs_list

stemmer = SnowballStemmer('english')

queryPath = "/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/query_desc.51-100.short.txt";

stopList = open("/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/stoplist.txt", 'r').read().split(
    "\n");

f3 = open('../cache/document_lengths.json')
length_of__document = json.load(f3)
f3.close()

f4 = open("../cache/all_doc_ids.txt")
all_doc_ids = f4.read().split("\n")

avg_document_length = get_average_doc_length()
total_documents = get_total_documents()
vocab_size = get_vocab_size()


def get_any_document(vector, term):
    for k, v in vector.items():
        if term in v.keys():
            return k


# returns how many times word occurs in this document
def getTermFreq(es, term, docId):
    res = es.get(index="ap89", id=docId)
    text = res['_source']['text'];
    words = re.findall('\w+', text.lower());
    count = words.count(term.lower())
    return count;


# returns how many documents contain this word
def getDocumentFreq(es, term):
    res = es.search(index="ap89", body={"query": {"match": {"text": term}}})
    return res['hits']['total']['value']


def get_query_unique_terms():
    all_unique_query_terms = []
    stopList = open("/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/stoplist.txt",
                    'r').read().split(
        "\n")
    with open(queryPath, 'r', encoding='iso-8859-1') as content_file:
        content = content_file.read();
        queryStrings = content.split("\n")[0:25]
        for query in queryStrings:
            query_id = query.split()[0][0:-1];
            query_document_will_removed = query[len(query_id) + 1:];  # ignore query number at begining 85.
            arr = query_document_will_removed.strip().replace('-', ' ').split(" ")
            arr = arr[3:]
            words = list(map(lambda val: val.strip().strip(',.\"()').lower(), arr))
            stopList += ["anticipate", "identify"]
            for word in words:
                if stopList.count(word) == 0:
                    all_unique_query_terms.append(word)
    return list(set(all_unique_query_terms))


def getDocumentLength(es, docId):
    print(docId)
    res = es.get(index="ap89", id=docId)
    text = res['_source']['text'];
    words = re.findall('\w+', text);
    count = len(words);
    return count;


def write_output(queryno, dict):
    query_content = ""
    rank = 1
    for k, v in dict.items():
        if rank > 1000:
            break
        op = str(queryno) + " Q0" + " " + str(k) + " " + str(rank) + " " + str(v) + " Exp";
        query_content += ("\n" + op)
        rank += 1
    return query_content


def jelnik_score(tf, ttf, docId):
    lambda_val = 0.6
    entire_corpus_words = avg_document_length * total_documents
    prob1 = lambda_val * tf / (length_of__document[docId])
    prob2 = (1 - lambda_val) * ttf / entire_corpus_words
    return math.log(prob1 + prob2)


def calculate_ttf(all_docs_for_this_word):
    _ttf = 0
    for doc in all_docs_for_this_word:
        _ttf += doc[0]
    return _ttf


with open("../query_desc.51-100.short.txt", 'r', encoding='iso-8859-1') as content_file:
    content = content_file.read();
    queryStrings = content.split("\n")[0:25];
    file_content = "";
    for query in queryStrings:
        score_query_doc = {}
        query_id = query.split()[0][0:-1];
        query_document_will_removed = query[len(query_id) + 1:];  # ignore query number at begining 85.
        # words = re.findall('\w+', query_document_will_removed.lower())[3:];  # ignore "documents will discuss"
        arr = query_document_will_removed.strip().replace('-', ' ').split(" ")
        arr = arr[3:]
        words = list(map(lambda val: val.strip().strip(',.\"()').lower(), arr))
        stopList += ["anticipate", "identify"]

        for word in words:
            if word.strip() != "" and stopList.count(word) == 0:
                # stemmed_word = stemmer.stem(word)
                stemmed_word = word
                print("word=", stemmed_word)
                # find list of all documents containing this word
                all_docs_for_this_word = get_all_docs_list(stemmed_word, False)
                ttf = calculate_ttf(all_docs_for_this_word)
                all_doc_ids_for_this_word = list(map(lambda doc: doc[1], all_docs_for_this_word))
                score_query_doc_keys = score_query_doc.keys()
                non_docs_word_ids = list(set(all_doc_ids) - set(all_doc_ids_for_this_word))

                for doc in all_docs_for_this_word:
                    tf = doc[0]
                    doc_id = doc[1]
                    word_score = jelnik_score(tf, ttf, doc_id)

                    if doc_id not in score_query_doc_keys:
                        score_query_doc[doc_id] = word_score
                    else:
                        score_query_doc[doc_id] += word_score

                for doc in non_docs_word_ids:
                    doc_id = doc
                    if length_of__document[doc_id] != 0:
                        word_score = jelnik_score(0, ttf, doc_id)
                        if doc_id not in score_query_doc_keys:
                            score_query_doc[doc_id] = word_score
                        else:
                            score_query_doc[doc_id] += word_score
        print("writing files")
        file_content += write_output(query_id,
                                     {k: v for k, v in
                                      sorted(score_query_doc.items(), key=lambda item: item[1], reverse=True)})

    with open("jelnik-output.txt", 'w',
              encoding='iso-8859-1') as output_file:
        file_content = file_content.strip()
        output_file.write(file_content)
