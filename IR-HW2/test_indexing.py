import json



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

f=open("indexing/catalogs/1-75merged.json")
big_catalog=json.load(f)
pr=read_inverted_list_without_file("torch","1-75merged",big_catalog)
print(pr)

