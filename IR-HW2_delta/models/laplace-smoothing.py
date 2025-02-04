import collections
import json
import math
import re

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

from nltk.stem.snowball import SnowballStemmer

from models.index_constants import get_average_doc_length, get_total_documents, get_vocab_size

stemmer = SnowballStemmer('english')

queryPath = "/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/query_desc.51-100.short.txt";

stopList = open("/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/stoplist.txt", 'r').read().split(
    "\n");

f3 = open('../cache/document_lengths.json')
length_of__document = json.load(f3)
f3.close()

f4 = open("../cache/all_doc_ids.txt")
all_doc_ids = f4.read().split("\n")


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es


es = connect_elasticsearch()
avg_document_length = get_average_doc_length()
total_documents = get_total_documents()
vocab_size = get_vocab_size()


def get_documents_list(es, term):
    scannedDocs = scan(es,
                       query={
                           "query": {
                               "match": {"text": term}
                           }
                       },
                       index="ap89");
    ids = list(map(lambda doc: doc['_id'], scannedDocs))

    return ids


def write_output(queryno, dict):
    query_content=""
    rank = 1
    for k, v in dict.items():
        if rank > 1000:
            break
        op = str(queryno) + " Q0" + " " + str(k) + " " + str(rank) + " " + str(v) + " Exp";
        query_content += ("\n"+op)
        rank += 1
    return query_content


def laplace_score(tf, docId):
    return math.log((1 + tf) / (length_of__document[docId] + vocab_size))


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

        f2 = open("../cache/cached-termvectors/" + query_id + ".json")
        all_term_vectors = json.load(f2)
        f2.close()

        for word in words:
            if word.strip() != "" and stopList.count(word) == 0:
                stemmed_word = stemmer.stem(word)
                print("word=", word)
                score_query_doc_keys = score_query_doc.keys();
                for doc in all_doc_ids:
                    doc_id = doc
                    if length_of__document[doc_id] == 0:
                        continue
                    if all_term_vectors[doc].get(stemmed_word) is not None:
                        tf = all_term_vectors[doc][stemmed_word]["term_freq"];
                        word_score = laplace_score(tf, doc_id)
                    else:
                        word_score = laplace_score(0, doc_id)

                    if doc_id not in score_query_doc_keys:
                        score_query_doc[doc_id] = word_score
                    else:
                        score_query_doc[doc_id] += word_score
        print("writing files")
        file_content += write_output(query_id,
                      {k: v for k, v in sorted(score_query_doc.items(), key=lambda item: item[1], reverse=True)})

    with open("laplace-output.txt", 'w',
              encoding='iso-8859-1') as output_file:
        file_content = file_content.strip()
        output_file.write(file_content)