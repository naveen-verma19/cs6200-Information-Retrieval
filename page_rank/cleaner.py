from urllib.parse import unquote


def cleaned_v(o):
    if "google.com/url?q=" in o:
        if o.count("&sa=") != 0:
            st = o.find("google.com/url?q=")
            en = o.find("&sa=")
            redirected_url = o[st + 17:en].strip()
            redirected_url = unquote(redirected_url)
            if not redirected_url.startswith("http"):
                print("invalid redirect",redirected_url)
                print(o)
                return o
            return redirected_url
        else:
            raise EOFError("invalid")
    else:
        return o


def clean_urls(fp,output_fp):
    li = fp.read().split("\n")
    # li_simpl = simp.read().split("\n")
    # li_non_rel = non_rel.read().split("\n")
    print("input size",len(li))
    linkgraph = {}
    for v in li:
        all_links = v.split(" ")
        main_link = all_links[0]
        cleaned = cleaned_v(main_link)
        outgoing_links = []
        if cleaned not in linkgraph:
            for o in all_links[1:]:
                redirected_url = cleaned_v(o)
                outgoing_links.append(redirected_url)
            linkgraph[cleaned] = outgoing_links
        else:
            print("Found duplicate",cleaned)
    print("size of mod linkgraph", len(linkgraph))

    for k, v in linkgraph.items():
        output_fp.write(k + " " + " ".join(v) + "\n")


simp = open("final_link_graph_outlinks.txt")
#
f2 = open("linkgraph3_cleaned.txt", "a")
clean_urls(simp,f2)