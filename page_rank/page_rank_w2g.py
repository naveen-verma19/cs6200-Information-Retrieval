import json
import math
import sys

cat = json.load(open('w2g_inlink_catalog.json', 'r'))
inlist = cat.keys()
f_always_opened = open('wt2g_inlinks', 'r')
outlinks = {}
sources = set()


def get_inlinks_line_list(url):
    t = cat[url]
    pos = t[0]
    offset = t[1]
    f_always_opened.seek(pos)
    lin = f_always_opened.read(offset)
    m_arr = lin.strip().split(" ")
    return list(map(lambda x: x.strip(), m_arr))


def isSingleLink(u, m):
    if m[0].strip() != u.strip() or m[0].strip() == "":
        raise EOFError("sss")
    if len(m) == 1:
        return True
    return False


for u in inlist:
    m = get_inlinks_line_list(u)
    if isSingleLink(u, m):
        sources.add(u)
    else:
        if m[0].strip() == "":
            raise EOFError("empty url")
    for inl in m[1:]:
        if inl != "":
            if inl not in outlinks:
                outlinks[inl] = 0
            outlinks[inl] += 1
print("sources,", len(sources))
non_source_links2 = inlist - sources
print("non_source links", len(non_source_links2))
sinks = non_source_links2 - outlinks.keys()
print("sinks", len(sinks))

print("all_links", len(inlist))

for s in sinks:
    if s in outlinks:
        print("error")

for sour in sources:
    if sour in non_source_links2:
        print("error")

PR = {}


def get_perplexity():
    s = 0
    for k, v in PR.items():
        s += -1 * math.log(v) / math.log(2) * v

    return pow(2, s)


def write_top_pages():
    sorted_PR = {k: v for k, v in
                 sorted(PR.items(), key=lambda item: item[1], reverse=True)}
    i = 0
    fj = open("dump.json", 'w')
    json.dump(sorted_PR, fj)

    f = open("page_rank_result", 'w')
    s = ""
    for k, v in sorted_PR.items():
        if i > 500:
            break
        inlinks_count = len(get_inlinks_line_list(k)[1:])
        if k not in outlinks:
            out_count = 0
        else:
            out_count = outlinks[k]

        s += k + " " + str(v) + " " + str(inlinks_count) + " " + str(out_count) + "\n"
        i += 1
    f.write(s)
    f.close()
    sys.exit()


N = len(inlist)
d = 0.85
for p in inlist:
    PR[p] = 1 / N
i = 0
count_convergence = 0
perplex1 = -1
perplex2 = -1

while True:
    if perplex2 == -1:
        perplex1 = get_perplexity()
    else:
        perplex1 = perplex2
    print("at", i, "perplexity", perplex1)
    i += 1
    sinkPR = 0
    for s in sinks:  # all pages which have no outlinks
        sinkPR += PR[s]
    newPR = {}
    for p in inlist:
        newPR[p] = (1 - d) / N
        newPR[p] += d * sinkPR / N
        if p in non_source_links2:  # p must have inlinks here
            inlink_list = get_inlinks_line_list(p)
            if not isSingleLink(p, inlink_list):
                for inl in inlink_list[1:]:
                    newPR[p] += d * PR[inl] / outlinks[inl]
    for p in inlist:
        PR[p] = newPR[p]

    perplex2 = get_perplexity()
    if int(perplex2 - perplex1) == 0:
        count_convergence += 1
        if count_convergence > 3:
            write_top_pages()
            break
