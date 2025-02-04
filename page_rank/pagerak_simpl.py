inlink = open("simple_graph.txt").read().split("\n")

inlink_d = {}
outlinks_count={}
for l in inlink:
    m = l.split(" ")
    inlink_d[m[0]] = m[1:]
    for inl in m[1:]:
        if inl not in outlinks_count:
            outlinks_count[inl]=[]
        outlinks_count[inl].append(m[0])




print(inlink_d)
print(outlinks_count)

