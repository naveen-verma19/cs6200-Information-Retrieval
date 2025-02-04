import json

cat = {}
with open("wt2g_inlinks", 'r') as ifile:
    while True:
        pos = ifile.tell()
        line = ifile.readline()
        if not line:
            break
        pos2 = ifile.tell()
        # if len(line.split(" "))!=1:
        m = line.strip().split(" ")
        url = m[0].strip()
        cat[url] = (pos, pos2 - pos)

print("cats", len(cat))
f = open("w2g_inlink_catalog.json", "w")
json.dump(cat, f)

# with open("simple_graph.txt",'r') as ifile2:
#    for u,t in cat.items():
#         pos=t[0]
#         offset=t[1]
#         ifile2.seek(pos)
#         line=ifile2.read(offset)
#         print(u,line)
