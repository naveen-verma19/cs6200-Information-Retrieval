import json
import os

all_doc_ids= open("all_doc_ids.txt").read().split("\n")

homePath = '/Users/naveen/Documents/Study/CS6200/Docker/Dropbox/IR_data/AP_DATA/ap89_collection/'
all_files = os.listdir(homePath)
text = filter(lambda x: x[0:4] == "ap89", all_files)
files = list(text)
print("length is ", len(files))
files.sort()
doc_count={}
for fileName in files:
    with open(homePath + fileName, 'r', encoding='iso-8859-1') as content_file:
        print("Reading file: ", fileName)
        content = content_file.read()
        docs = content.split("<DOC>")[1:]  # docs[0] will be empty rest all are documents
        doc_count[fileName]=len(docs)

f=open('doc_count.json','w')    ;
json.dump(doc_count, f)
f.close()