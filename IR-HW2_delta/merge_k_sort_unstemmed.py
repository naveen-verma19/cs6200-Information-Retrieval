import json
import os

import ray as ray
from sortedcontainers import SortedSet

from test_merge_ksorted import merge_k_arrays
inverted_list_directory="indexing/unstemmed/inverted-lists/"
catalogs_directory="indexing/unstemmed/catalogs/"

def word_exists(word, file_number):
    f = open( catalogs_directory+ str(file_number) + ".json", 'r')
    cat = json.load(f)
    f.close()
    return word in cat.keys()


def read_inverted_list_without_file(word, j, jth_catalog):
    if word in jth_catalog.keys():
        val = jth_catalog[word]
        start = val[0]
        offset = val[1]

        f2 = open(inverted_list_directory + str(j) + ".json", 'r')
        f2.seek(start)
        read_line = f2.read(offset)
        f2.close()

        list_val = read_line.strip()
        js = json.loads(list_val)

        if type(js) != list:
            raise FileNotFoundError("invalid read")

        return js
    return []


def read_inverted_list_without_file_convert_to_tuples(word, j, jth_catalog, b=10):
    if word in jth_catalog.keys():
        val = jth_catalog[word]
        start = val[0]
        offset = val[1]

        f2 = open(inverted_list_directory + str(j) + ".txt", 'r')
        f2.seek(start)
        read_line = f2.read(offset)
        f2.close()
        arr = read_line.strip().split()
        list_final = []
        i = 0
        while i < len(arr):
            count = int(arr[i], b)
            substr = arr[i + 1:i + 2 + count]
            i += count + 2
            list_final.append((count, " ".join(substr)))
        return list_final
    return []


# print(read_inverted_list("grunt",1))
def get_catalogs_size():
    all_catalog_files = list(filter(lambda f: f.endswith(".json"), os.listdir(catalogs_directory)))
    return len(all_catalog_files)


def load_all_catalogs(start, end):
    # all_catalog_files = list(filter(lambda f: f.endswith(".json"), os.listdir("indexing/catalogs")))
    #
    # length = len(all_catalog_files)
    all_catalogs = {}
    for i in range(start, end + 1):
        with open(catalogs_directory + str(i) + ".json") as curr_file:
            all_catalogs[i] = json.load(curr_file)

    return all_catalogs


def get_vocabulary(start_batch=1, end_batch=75):
    all_words = set()
    # all_catalog_files = list(filter(lambda f: f.endswith(".json"), os.listdir("indexing/catalogs")))
    for i in range(start_batch, end_batch + 1):
        with open(catalogs_directory + str(i) + ".json") as curr_file:
            loaded = json.load(curr_file).keys()
            all_words.update(loaded)
    return all_words


whole_catalog = {}


def toHex(i):
    return hex(i)[2:]


def string_of_ints_tohexs(string):
    hex_arr = []
    arr = string.strip().split()
    for val in arr:
        hex_arr.append(toHex(int(val.strip())))
    final = " ".join(hex_arr).strip()
    return final



def create_cat(start_batch, end_batch, final_file_name):
    catalog_path = catalogs_directory + str(final_file_name) + ".json"
    with open(catalog_path, 'w') as catalog_file:
        json.dump(whole_catalog, catalog_file)

convTable = (
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V')


def to32(n):
    a = []
    if n == 0:
        return '0'
    while n > 0:
        r = n % 32
        a.append(convTable[r])
        n = n // 32
    a.reverse()
    return "".join(a)


def string_of_ints_tobase32(string):
    hex_arr = []
    arr = string.strip().split()
    for val in arr:
        hex_arr.append(to32(int(val.strip())))
    final = " ".join(hex_arr).strip()
    return final


def write_merged_term_list(fp, merged_list, term):
    to_print = ""
    for tup in merged_list:
        to_print += to32(tup[0]) + " " + string_of_ints_tobase32(tup[1]) + " "
    start = fp.tell()
    fp.write(to_print.strip())
    end = fp.tell()
    whole_catalog[term] = (start, end - start)


def write_merged_term_list_from32(fp, merged_list, term):
    to_print = ""
    for tup in merged_list:
        to_print += to32(tup[0]) + " " + tup[1] + " "
    start = fp.tell()
    fp.write(to_print.strip())
    end = fp.tell()
    whole_catalog[term] = (start, end - start)

# merges  base 10 files to a new base 32 file
@ray.remote
def merge_all_inverted_lists(start_batch, end_batch, final_file_name):
    all_catalogs = load_all_catalogs(start_batch, end_batch)
    fp = open(inverted_list_directory + str(final_file_name) + ".txt", 'w')
    counted_words = SortedSet()
    for i in range(start_batch, end_batch + 1):
        print("batch" + str(i))
        words = all_catalogs[i].keys()
        for token in words:
            if not (token in counted_words):  # O(1)
                counted_words.add(token)  # O(logn)
                list_of_lists = []
                this_list = read_inverted_list_without_file_convert_to_tuples(token, i, all_catalogs[i])
                if len(this_list) == 0:
                    raise KeyboardInterrupt("word should be in this batch")
                list_of_lists.append(this_list)
                for j in range(1 + i, end_batch + 1):
                    read_list = read_inverted_list_without_file_convert_to_tuples(token, j, all_catalogs[j])
                    if len(read_list) != 0:
                        list_of_lists.append(read_list)
                if len(list_of_lists) == 1:
                    write_merged_term_list(fp, list_of_lists[0], token)
                else:
                    write_merged_term_list(fp, merge_k_arrays(list_of_lists), token)
    create_cat(start_batch, end_batch, final_file_name)
    return final_file_name

#Merges base 32 files to a new base 32 file
@ray.remote
def merge_all_inverted_lists_from32(start_batch, end_batch, final_file_name):
    all_catalogs = load_all_catalogs(start_batch, end_batch)
    fp = open(inverted_list_directory + str(final_file_name) + ".txt", 'w')
    counted_words = SortedSet()
    for i in range(start_batch, end_batch + 1):
        print("batch" + str(i))
        words = all_catalogs[i].keys()
        for token in words:
            if not (token in counted_words):  # O(1)
                counted_words.add(token)  # O(logn)
                list_of_lists = []
                this_list = read_inverted_list_without_file_convert_to_tuples(token, i, all_catalogs[i], 32)
                if len(this_list) == 0:
                    raise KeyboardInterrupt("word should be in this batch")
                list_of_lists.append(this_list)
                for j in range(1 + i, end_batch + 1):
                    read_list = read_inverted_list_without_file_convert_to_tuples(token, j, all_catalogs[j], 32)
                    if len(read_list) != 0:
                        list_of_lists.append(read_list)
                if len(list_of_lists) == 1:
                    write_merged_term_list_from32(fp, list_of_lists[0], token)
                else:
                    write_merged_term_list_from32(fp, merge_k_arrays(list_of_lists), token)
    create_cat(start_batch, end_batch, final_file_name)




# merge_all_inverted_lists(1,75,108)
#
# def create_catalog_merged():
#     batch_current = "1-75merged"
#     catalog = {}
#     print("writing catalog.." + str(batch_current))
#     index_path = "indexing/inverted-lists/" + str(batch_current) + ".txt"
#     catalog_path = "indexing/catalogs/" + str(batch_current) + ".json"
#     current_pos = 0
#     num_lines = 0
#     with open(index_path, 'r') as infile:
#         for line in infile:
#             num_lines += 1
#             if num_lines % 1000 == 0:
#                 print("1000 lines cataloged, total=" + str(num_lines))
#             arr = line.strip().split(":")
#             term = arr[0]
#             size_of_line = len(line)
#             catalog[term] = (current_pos, size_of_line)
#             current_pos += size_of_line
#         print("total=" + str(num_lines))
#     with open(catalog_path, 'w') as catalog_file:
#         json.dump(catalog, catalog_file)
