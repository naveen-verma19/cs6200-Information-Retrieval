import json
import os

from sortedcontainers import SortedSet


def process_doc_lengths():
    f = open("../indexing/stemmed/catalogs/108.json", 'r')
    big_catalog = json.load(f)
    f.close()

    with open(os.path.dirname(__file__) + "/../hash_to_doc_ids.json") as htod:
        hash_to_doc = json.load(htod)

    all_doc_ids_set = set(open("../all_doc_ids.txt").read().split("\n"))
    doc_length = {}
    counted_ids = set()
    words_processed = 0
    f2 = open("../indexing/stemmed/inverted-lists/108.txt", 'r')

    for k, v in big_catalog.items():
        start = v[0]
        offset = v[1]
        words_processed += 1
        if words_processed % 1000 == 0:
            print("1000 words read, total=" + str(words_processed))
        f2.seek(start)
        read_line = f2.read(offset)
        arr = read_line.strip().split()

        i = 0
        while i < len(arr):
            count = int(arr[i], 32)
            doc_id = hash_to_doc[str(int(arr[i + 1], 32))]
            if doc_id not in counted_ids:
                counted_ids.add(doc_id)
                doc_length[doc_id] = count
            else:
                doc_length[doc_id] += count
            i += count + 2

    rest = all_doc_ids_set - counted_ids
    for doc_id in rest:
        doc_length[doc_id] = 0
    f = open('../cache/document_lengths.json', 'w')
    json.dump(doc_length, f)
    f.close()


# process_doc_lengths()

def test123():
    f = open("../indexing/stemmed/catalogs/108.json", 'r')
    big_catalog = json.load(f)
    f.close()

    with open(os.path.dirname(__file__) + "/../hash_to_doc_ids.json") as htod:
        hash_to_doc = json.load(htod)

    all_doc_ids_set = set(open("../all_doc_ids.txt").read().split("\n"))
    doc_length = {}
    counted_ids = set()
    words_processed = 0
    f2 = open("../indexing/stemmed/inverted-lists/108.txt", 'r')
    maxt = 0
    sum = 0
    for k, v in big_catalog.items():
        start = v[0]
        offset = v[1]
        words_processed += 1
        if words_processed % 1000 == 0:
            print("1000 words read, total=" + str(words_processed))
        f2.seek(start)
        read_line = f2.read(offset)
        arr = read_line.strip().split()

        i = 0
        while i < len(arr):
            count = int(arr[i], 32)
            doc_id = (int(arr[i + 1], 32))
            posns = arr[i + 2:i + 2 + count]
            posns = list(map(lambda p: int(p, 32), posns))
            # maxt=max(count,max(posns),maxt)
            i += count + 2
            sum += (2 + len(posns)) * 2 * 3
    print(sum)


test123()
