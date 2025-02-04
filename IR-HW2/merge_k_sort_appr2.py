import json
import os

from sortedcontainers import SortedSet

from test_merge_ksorted import merge_k_arrays


def word_exists(word, file_number):
    f = open("indexing/catalogs/" + str(file_number) + ".json", 'r')
    cat = json.load(f)
    f.close()
    return word in cat.keys()


# INEFFICIENT METHOD
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


def read_inverted_list_without_file(word, j, jth_catalog):
    if word in jth_catalog.keys():
        val = jth_catalog[word]
        start = val[0]
        offset = val[1]

        f2 = open("indexing/inverted-lists/" + str(j) + ".json", 'r')
        f2.seek(start)
        read_line = f2.read(offset)
        f2.close()

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
    # vocab = get_vocabulary(start_batch, end_batch)
    all_catalogs = load_all_catalogs()
    fp = open("indexing/inverted-lists/" + str(start_batch) + "-" + str(end_batch) + "merged.json", 'w')

    counted_words = SortedSet()
    for i in range(start_batch, end_batch + 1):
        print("batch" + str(i))
        words = all_catalogs[i].keys()
        for token in words:
            if not (token in counted_words):  # O(1)
                counted_words.add(token)  # O(logn)
                list_of_lists = []
                this_list = read_inverted_list_without_file(token, i, all_catalogs[i])
                if len(this_list) == 0:
                    raise KeyboardInterrupt("word should be in this batch")
                list_of_lists.append(this_list)

                for j in range(start_batch + i, end_batch + 1):
                    read_list = read_inverted_list_without_file(token, j, all_catalogs[j])
                    if len(read_list) != 0:
                        list_of_lists.append(read_list)
                if len(list_of_lists) == 1:
                    write_merged_term_list(fp, list_of_lists[0], token)
                else:
                    write_merged_term_list(fp, merge_k_arrays(list_of_lists), token)

def create_catalog_merged():
    batch_current="1-75merged"
    catalog = {}
    print("writing catalog.." + str(batch_current))
    index_path = "indexing/inverted-lists/" + str(batch_current) + ".json"
    catalog_path = "indexing/catalogs/" + str(batch_current) + ".json"
    current_pos = 0
    num_lines = 0
    with open(index_path, 'r') as infile:
        for line in infile:
            num_lines += 1
            if num_lines % 1000 == 0:
                print("1000 lines cataloged, total=" + str(num_lines))
            arr = line.strip().split(":")
            term = arr[0]
            size_of_line = len(line)
            catalog[term] = (current_pos, size_of_line)
            current_pos += size_of_line
        print("total="+str(num_lines))
    with open(catalog_path, 'w') as catalog_file:
        json.dump(catalog, catalog_file)

# merge_all_inverted_lists(1, 75)
# create_catalog_merged()
