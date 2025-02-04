import collections
import json
import math
import os
import re

from nltk.stem.snowball import SnowballStemmer

from test_indexing import get_all_docs_list

stemmer = SnowballStemmer('english')


from models.index_constants import get_average_doc_length, get_total_documents


queryPath = "/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/query_desc.51-100.short.txt"

stopList = open("/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/stoplist.txt", 'r').read().split(
    "\n")

print("Loading document lengths..")
f3 = open(os.path.join(os.path.dirname(__file__), '../cache/document_lengths.json'))
length_of__document = json.load(f3)
f3.close()


avg_document_length = get_average_doc_length()
total_documents = get_total_documents()




def get_documents_list_local(vector, term):
    ids = []
    for k, v in vector.items():
        if term in v.keys():
            ids.append(k)
    return ids


# okapi score(query_term, document)
def okapi_tf(documentId, tf, df):
    length = length_of__document[documentId]
    return tf / (tf + 0.5 + 1.5 * length / avg_document_length) * math.log(total_documents / df)


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


with open(os.path.join(os.path.dirname(__file__),"../query_desc.51-100.short.txt"), 'r', encoding='iso-8859-1') as content_file:
    content = content_file.read()
    queryStrings = content.split("\n")[0:25]
    file_content = "";
    for query in queryStrings:
        score_query_doc = {}
        query_id = query.split()[0][0:-1]
        query_document_will_removed = query[len(query_id) + 1:]  # ignore query number at begining 85.
        arr = query_document_will_removed.strip().replace('-', ' ').split(" ")
        arr = arr[3:]
        words = list(map(lambda val: val.strip().strip(',.\"()').lower(), arr))
        stopList += ["anticipate", "identify"]

        # f2 = open("../cache/cached-termvectors/"+query_id+".json")
        # all_term_vectors = json.load(f2)
        # f2.close()

        for word in words:
            if word.strip() != "" and stopList.count(word) == 0:
                stemmed_word = stemmer.stem(word)
                # stemmed_word=word
                print("word=", stemmed_word)
                # find list of all documents containing this word
                all_docs_for_this_word = get_all_docs_list(stemmed_word)
                # find df
                if len(all_docs_for_this_word) != 0:
                    print("Termvector calculated, size=", len(all_docs_for_this_word))
                    df = len(all_docs_for_this_word)
                    score_query_doc_keys = score_query_doc.keys()
                    for doc in all_docs_for_this_word:
                        tf = doc[0]
                        doc_id = doc[1]
                        word_score = okapi_tf(doc_id, tf, df)
                        # if score_query_doc.get(doc_id) is None:
                        if doc_id not in score_query_doc_keys:
                            score_query_doc[doc_id] = word_score
                        else:
                            score_query_doc[doc_id] += word_score
        print("writing files")
        file_content += write_output(query_id,
                                     {k: v for k, v in
                                      sorted(score_query_doc.items(), key=lambda item: item[1], reverse=True)})

    with open("okapi-idf-output.txt", 'w',
              encoding='iso-8859-1') as output_file:
        file_content=file_content.strip()
        output_file.write(file_content)