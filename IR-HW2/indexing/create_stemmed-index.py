import json
import os

from indexing.create_catalog import create_catalog
from indexing.doc_dictionaries import get_dict_stopped_stemmed
from indexing.reverse_insert import reverse_insort
from elasticsearch import Elasticsearch




def store_record_myIndex(doc_number, text):
    doc_dict = get_dict_stopped_stemmed(text)
    for k, v in doc_dict.items():
        if k not in term_dict.keys():
            term_dict[k] = [(len(v), doc_number, v)]
        else:
            reverse_insort(term_dict[k], (len(v), doc_number, v))
        # term_dict[k].append((len(v), doc_number, v))
        # term_dict[k].sort(key=lambda tup: tup[0], reverse=True)


def write_batch(batch_current, term_dict):
    print("writing batch.." + str(batch_current))
    f = open("inverted-lists/" + str(batch_current) + ".json", 'w')
    to_print = ""
    for k, v in term_dict.items():
        to_print += k + ":" + json.dumps(v) + "\n"
    f.write(to_print)
    f.close()


homePath = '/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/ap89_collection/'
all_files = os.listdir(homePath)
text = filter(lambda x: x[0:4] == "ap89", all_files)
files = list(text)
files.sort()

docs_read = 0
batch = 1
term_dict = {}
for fileName in files[0:5]:
    with open(homePath + fileName, 'r', encoding='iso-8859-1') as content_file:
        print("Reading file: ", fileName)
        content = content_file.read()
        docs = content.split("<DOC>")[1:]  # docs[0] will be empty rest all are documents
        for doc in docs:
            doc_number_start = doc.find("<DOCNO>")
            doc_number_end = doc.find("</DOCNO>")
            doc_number = doc[doc_number_start + 7:doc_number_end].strip();
            this_docs_Text = "";
            texts = doc.split("<TEXT>")[1:]
            for text in texts:
                text_end = text.find("</TEXT>")
                subText = text[0:text_end].strip()
                this_docs_Text += subText + " "
            store_record_myIndex(doc_number, this_docs_Text)
            docs_read += 1
    if docs_read >= 1000:
        write_batch(batch, term_dict)
        create_catalog(batch)
        docs_read = 0
        term_dict = {}
        batch += 1
# remaining batch <1000
write_batch(batch, term_dict)
create_catalog(batch)
