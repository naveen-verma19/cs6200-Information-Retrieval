import math

inlink = open("wt2g_inlinks").read().split("\n")
inlink_d = {}
outlinks = {}
sources = set()
for l in inlink:
    m = l.strip().split(" ")
    if len(m) == 1:
        if l.strip() != "":
            sources.add(l.strip())
    else:
        if m[0].strip() == "":
            raise EOFError("empty url")
        inlink_d[m[0]] = m[1:]
    for inl in m[1:]:
        if inl.strip() != "":
            if inl not in outlinks:
                outlinks[inl] = []
            outlinks[inl].append(m[0])

print("sources (no inlinks)", len(sources))
inlinks_left_set_no_source = set(inlink_d)
outlinks_left_set = set(outlinks)
all_links = inlinks_left_set_no_source.union(sources)
print("all links set", len(all_links))
print("non source links", len(inlinks_left_set_no_source))
print("all links which have outgoing links", len(outlinks_left_set))

sinks = inlinks_left_set_no_source - outlinks_left_set
print("empty", sinks.intersection(sources))  # empty check
rev_sink = outlinks_left_set - inlinks_left_set_no_source  # source pages
print("empty here", rev_sink - sources)  # empty check
print("rev_sink is", len(rev_sink))  #
print("all sinks(no outlinks)", len(sinks))

print("outlinks_list",len(outlinks))


for s in sinks:
    if s in outlinks_left_set:
        print("error")
for sour in sources:
    if sour in inlinks_left_set_no_source:
        print("error")

PR = {}


def get_perplexity():
    s = 0
    for k, v in PR.items():
        s += -1 * math.log(v) / math.log(2) * v

    return pow(2, s)


N = len(all_links)
d = 0.85
for p in all_links:
    PR[p] = 1 / N
i = 0
while i < 7:
    print("perplexity at", i, get_perplexity())
    i += 1
    sinkPR = 0
    for s in sinks:  # all pages which have no outlinks
        sinkPR += PR[s]
    newPR = {}
    for p in all_links:
        newPR[p] = (1 - d) / N
        newPR[p] += d * sinkPR / N
        if p in inlinks_left_set_no_source:  # p must have inlinks here
            for inl in inlink_d[p]:
                newPR[p] += d * PR[inl] / len(outlinks[inl])
    for p in all_links:
        PR[p] = newPR[p]
