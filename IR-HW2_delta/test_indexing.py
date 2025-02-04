import json
import os
import sys

from delta_encode import delta_decode

stemmed_merged_catalog_path = os.path.dirname(__file__) + "/indexing/stemmed/catalogs/108.json"
stemmed_merged_inverted_path = os.path.dirname(__file__) + "/indexing/stemmed/inverted-lists/"

unstemmed_merged_catalog_path = os.path.dirname(__file__) + "/indexing/unstemmed/catalogs/108.json"
unstemmed_merged_inverted_path = os.path.dirname(__file__) + "/indexing/unstemmed/inverted-lists/"


def convert_to_list_unhashed(line):
    arr = line.strip().split()
    list_final = []
    i = 0
    while i < len(arr):
        count = int(arr[i])
        doc_id = arr[i + 1]
        posns = arr[i + 2:i + 2 + count]
        i += count + 2
        list_final.append((count, doc_id, posns))
    return list_final


def read_inverted_list_without_file_unhashed(word, jth_catalog, inverted_file_pointer):
    with open(os.path.dirname(__file__) + "/hash_to_doc_ids.json") as htod:
        hash_to_doc = json.load(htod)

    f2=inverted_file_pointer
    if word in jth_catalog.keys():
        val = jth_catalog[word]
        start = val[0]
        offset = val[1]

        f2.seek(start)
        read_line = f2.read(offset)
        f2.close()

        arr = read_line.strip().split()
        list_final = []
        i = 0
        while i < len(arr):
            try:
                count = int(arr[i], 32)
                doc_id = hash_to_doc[str(int(arr[i + 1], 32))]
                posns = arr[i + 2:i + 2 + count]
                posns = list(map(lambda p: int(p, 32), posns))
                delta_decode(posns)
                i += count + 2
                list_final.append((count, doc_id, posns))
            except:
                print(i, arr[i], len(arr), arr)
                break
        return list_final
    return []


def get_all_docs_list(term, stemming=True):
    # print(os.path.join(os.path.dirname(__file__), "/indexing/catalogs/1-75merged.json"))
    if stemming:
        f = open(stemmed_merged_catalog_path, 'r')
        f2 = open(stemmed_merged_inverted_path + "108.txt", 'r')
    else:
        f = open(unstemmed_merged_catalog_path, 'r')
        f2 = open(unstemmed_merged_inverted_path + "108.txt", 'r')

    big_catalog = json.load(f)
    f.close()
    pr = read_inverted_list_without_file_unhashed(term,big_catalog, f2)
    return pr


def get_vocab(stemming=True):
    if stemming:
        f = open(stemmed_merged_catalog_path, 'r')
    else:
        f = open(unstemmed_merged_catalog_path, 'r')
    big_catalog = json.load(f)
    f.close()
    return len(big_catalog)




# f = open(stemmed_merged_catalog_path, 'r')
# big_catalog = json.load(f)
# f.close()
# fl=read_inverted_list_without_file_unhashed("sheriff","108",big_catalog)
# print(fl)

# words = list(big_catalog.keys())
# words.sort()
# count = 1
# sumw = 0
# for k, v in big_catalog.items():
#     if len(k)==2:
#         li=read_inverted_list_without_file_unhashed(k,"1-75merged",big_catalog)
#         print(str(k) + " " + str(len(li)))

# sumw=0
# for i in range(1,168020):
#     sumw += len(str(i))
# print(sumw)
