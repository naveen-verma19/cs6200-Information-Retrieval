import collections
import json
import math
import re

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english')

queryPath = "/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/query_desc.51-100.short.txt";

query_remover="query_mod.txt"




# f2=open('term_vectors.json')
# all_term_vectors=json.load(f2)
# f2.close()
#
# f3=open('document_lengths.json')
# length_of__document=json.load(f3)
# f3.close()

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es


es = connect_elasticsearch()


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

def get_top_1000(es,query):
    res = es.search(index="ap89",
                    body={
                        "size": 1000,
                        "query":
                              {
                                  "match":
                                   {"text": query}
                               }
                          })
    return res['hits']['hits']

def get_all_documents(es):
    scannedDocs = scan(es,
                       query={
                           "query": {
                               "match_all": {}
                           }
                       },
                       index="ap89");
    ids = list(map(lambda doc: doc['_id'], scannedDocs))

    return ids


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


# get average document length in entire corpus
def getAverageDocumentLength(es):
    all_docs = get_all_documents(es)
    length = 0
    for doc in all_docs:
        length += getDocumentLength(es, doc);
    return length / len(all_docs)


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

    # for query in queryStrings:
    #     score_query_doc = {}
    #     query_id = query.split()[0][0:-1];
    #     query_number_removed = query[len(query_id)+1:];  # ignore query number at begining 85.
    #     # arr = query_number_removed.strip().replace('-',' ').split(" ")
    #     arr = query_number_removed.strip().split(" ")
    #
    #     arr=arr[3:]
    #     # words = list(map(lambda val: val.strip().strip(',.\"()').lower(), arr))
    #     if arr.count("anticipate")>0:
    #         arr.remove("anticipate")
    #     if arr.count("identify")>0:
    #         arr.remove("identify")
    #
    #     mod_query=" ".join(arr)



def load_query_file():
    content_file=open("../query_desc.51-100.short.txt", 'r', encoding='iso-8859-1')
    content = content_file.read();
    content_file.close()
    return content

def start(content):
    stopList = open("/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/stoplist.txt",
                    'r').read().split(
        "\n");
    # mod_queries=open("elastisearch-modified_queries.txt",'r').read().split("\n");
    queryStrings = content.split("\n")[0:25];
    file_content = "";
    for query in queryStrings:
        score_query_doc = {}
        query_id = query.split()[0][0:-1]
        query_document_will_removed = query[len(query_id) + 1:]  # ignore query number at begining 85.
        arr = query_document_will_removed.strip().replace('-', ' ').split(" ")
        arr = arr[3:]
        words = list(map(lambda val: val.strip().strip(',.\"()').lower(), arr))
        stopList += ["anticipate", "identify"]
        stemmed_query=""
        for word in words:
            if word.strip() != "" and stopList.count(word) == 0:
                stemmed_word = stemmer.stem(word)
                print("word=", stemmed_word)
                stemmed_query+=stemmed_word+" "
        stemmed_query=stemmed_query.strip()

        all_docs_for_this_word= get_top_1000(es,stemmed_query)
        for doc in all_docs_for_this_word:
            score_query_doc[doc['_id']]=doc['_score']
        print("writing")
        file_content+= write_output(query_id,
                      {k: v for k, v in sorted(score_query_doc.items(), key=lambda item: item[1], reverse=True)})

    with open("elastisearch-output.txt", 'w',
              encoding='iso-8859-1') as output_file:
        file_content=file_content.strip()
        output_file.write(file_content)

if __name__ == '__main__':
    c = load_query_file()
    start(c)
