import json

from test_indexing import get_vocab


def calculate():
    f3 = open("../cache/document_lengths.json")
    length_of__document = json.load(f3)
    f3.close()
    return length_of__document


def get_average_doc_length():
    length_of__document = calculate()
    length = 0
    for k, v in length_of__document.items():
        length += v

        # 21051185

    # print("total words="+ str(length))

    total_docs = len(open("../cache/all_doc_ids.txt").read().split("\n"))

    # print("total docs="+str(total_docs))
    average = length / total_docs

    # print("average doc length="+str(average))
    return average


def get_total_documents():
    return len(open("../cache/all_doc_ids.txt").read().split("\n"))


def get_vocab_size():
    return get_vocab()
