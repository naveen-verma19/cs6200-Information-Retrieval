f2 = open("linkgraph3_cleaned.txt", "r")
#
lines = f2.read().split("\n")
main_links = set(map(lambda x: x.split(" ")[0].strip(), lines))
print("all links in linkgrph", len(main_links))
inlinks_inbetween = {}
inlinks_sources = {}
inlinks_sinks = {}

source_links = set(main_links)  # all pages that are on left and not on right


def insert(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)


for v in lines:
    all_links = v.split(" ")
    main_link = all_links[0]
    for o in all_links[1:]:
        if o in main_links:  # page on right and on left
            insert(inlinks_inbetween, o, main_link)
        else:
            # page on right but not on left (sink)
            insert(inlinks_sinks, o, main_link)
        if o in source_links:
            source_links.remove(o)

print("source_pages", len(source_links))
print("inbetween_pages", len(inlinks_inbetween))
print("sink_pages", len(inlinks_sinks))

combined_inlink_dict = {}
for s in source_links:
    combined_inlink_dict[s] = []

for k, v in inlinks_inbetween.items():
    combined_inlink_dict[k] = v

for k, v in inlinks_sinks.items():
    combined_inlink_dict[k] = v

print("combined_dict",len(combined_inlink_dict))


output_fp = open("inlinks_new.txt", "w")

for k, v in combined_inlink_dict.items():
    output_fp.write(k + " " + " ".join(v) + "\n")
