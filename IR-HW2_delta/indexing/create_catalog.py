import json
import sys

#UNUSED
def create_catalog(batch_current):
    catalog = {}
    print("writing catalog.." + str(batch_current))
    index_path = "inverted-lists/" + str(batch_current) + ".json"
    catalog_path = "catalogs/" + str(batch_current) + ".json"
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
        print("total=" + str(num_lines))
    with open(catalog_path, 'w') as catalog_file:
        json.dump(catalog, catalog_file)


