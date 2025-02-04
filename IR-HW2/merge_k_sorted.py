import json
import os

from test_merge_ksorted import merge_k_arrays


def word_exists(word, file_number):
    f = open("indexing/catalogs/" + str(file_number) + ".json", 'r')
    cat = json.load(f)
    f.close()
    return word in cat.keys()


# no need to use above method before using this
def read_inverted_list(word, file_number):
    f = open("indexing/catalogs/" + str(file_number) + ".json", 'r')
    cat = json.load(f)
    f.close()
    if word in cat.keys():
        val = cat[word]
        start = val[0]
        offset = val[1]

        f2 = open("indexing/inverted-lists/" + str(file_number) + ".json", 'r')
        f2.seek(start)
        read_line = f2.read(offset)

        arr = read_line.split(":")
        key = arr[0].strip()
        if key != word:  # if catalog data is corrupted
            raise FileNotFoundError("word not found at this pointer")
        list_val = arr[1].strip()
        js = json.loads(list_val)
        return js
    return []


# print(read_inverted_list("grunt",1))
def get_catalogs_size():
    all_catalog_files = list(filter(lambda f: f.endswith(".json"), os.listdir("indexing/catalogs")))
    return len(all_catalog_files)


def load_all_catalogs():
    all_catalog_files = list(filter(lambda f: f.endswith(".json"), os.listdir("indexing/catalogs")))

    length = len(all_catalog_files)
    all_catalogs = {}
    for i in range(1, length + 1):
        with open("indexing/catalogs/" + str(i) + ".json") as curr_file:
            all_catalogs[i] = json.load(curr_file)

    return all_catalogs


def get_vocabulary(start_batch=1, end_batch=75):
    all_words = set()
    all_catalog_files = list(filter(lambda f: f.endswith(".json"), os.listdir("indexing/catalogs")))
    for i in range(start_batch, end_batch + 1):
        with open("indexing/catalogs/" + str(i) + ".json") as curr_file:
            loaded = json.load(curr_file).keys()
            all_words.update(loaded)
    return all_words


def write_merged_term_list(fp, merged_list, term):
    to_print = term + ":" + json.dumps(merged_list) + "\n"
    fp.write(to_print)


def merge_all_inverted_lists(start_batch, end_batch):
    vocab = get_vocabulary(start_batch, end_batch)
    size = len(vocab)
    fp = open("indexing/inverted-lists/"+str(start_batch)+"-"+str(end_batch)+"merged.json", 'w')
    c = 1
    p=0
    for token in vocab:
        per=int(c/size)*100
        if p!=per:
            p=per
            print(p)
        c += 1
        list_of_lists = []
        for i in range(start_batch, end_batch + 1):
            read_list = read_inverted_list(token, i)
            if len(read_list) != 0:
                list_of_lists.append(read_list)
        if len(list_of_lists) == 1:
            write_merged_term_list(fp, list_of_lists[0], token)
        else:
            write_merged_term_list(fp, merge_k_arrays(list_of_lists), token)


merge_all_inverted_lists(1,4)
