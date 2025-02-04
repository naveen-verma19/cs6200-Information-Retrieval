import json
import os
import pickle
import queue
import sys
import time
import traceback

import requests
from adblockparser import AdblockRules
from bs4 import BeautifulSoup
from fibheap import makefheap, fheappush

from crawler_lib import cannonical, get_text, get_GET_response, get_HEAD_response, get_exact_outgoing_links, \
    get_domain

f = open("majestic_million.json", 'r')
whitelist_domains = json.load(f)
f.close()
BATCH_SIZE = 100
f = open("seed_urls.json", 'r')
seed_urls = json.load(f)["urls"]
f.close()
f_linkgraph = open("linkgraph.txt", 'a', encoding="utf-8")

# print("loading adblocker regex..")
# with open('adblock_rules.dictionary', 'rb') as config_dictionary_file:
#     # Step 3
#     adblock_rules = AdblockRules([])
#     adblock_rules = pickle.load(config_dictionary_file)

keyw = open("keywords.txt").read().split("\n")
keywords = []
for w in keyw:
    if w.strip() != '':
        keywords.append(w.strip())
keywords_length = len(keywords)

fibheap = makefheap()
fib_Hash = {}  # keep track of nodes in fibheap add while enque and delete while dequeue

stored_urls = set()  # all urls that i have already stored + cache from link-graph
processed_batch_file_content = []  # processed files in this batch about to be stored as soon as count>200
processed_batch_html = {}

processing_batch_urls = {}  # hash of url->nodes
processing_batch_queue = []  # dequeued batch(queue) of 200 from the fibheap


# returns 0 if irrevelant otherwise score between 0.01-0.09 in 0.01 range
def get_relevance_factor(text):
    if len(text.strip()) == 0:
        return 0
    lower = text.lower()
    if "nuclear" not in lower:
        return 0
    count = 1
    tf_nuclear = lower.count("nuclear")
    total_words = lower.count(" ")
    if tf_nuclear / total_words < 0.005:
        return 0
    overall_tf_count = tf_nuclear
    other_words_tf_count = 0
    for w in keywords:
        if w in lower:
            count += 1
            tfcount = lower.count(w)
            other_words_tf_count += tfcount
    if count < 2:
        return 0
    if other_words_tf_count < 0.3 * tf_nuclear:
        return 0
    overall_tf_count += other_words_tf_count
    return overall_tf_count / total_words  # 0.01 range


def get_relevance_count(link_text):
    if len(link_text.strip()) == 0:
        return 0
    lower = link_text.lower()
    count = 0
    if "nuclear" in lower:
        count = 1
    for w in keywords:
        if w in lower:
            count += 1
    return count


def store_docs(url, title, text, header, html):
    print("storing", url)
    global processed_batch_file_content
    global processed_batch_html
    content = "<DOC>\n"
    content += "<DOCNO>" + url + "</DOCNO>\n"
    if title != "":
        content += "<HEAD>" + title + "</HEAD>\n"
    content += "<TEXT>" + text + "</TEXT>\n</DOC>"

    processed_batch_file_content.append({
        "url-can": url,
        "file_content": content
    })
    processed_batch_html[url] = {
        "raw-html": html,
        "header": json.dumps(header.__dict__['_store'])
    }

    if len(processed_batch_file_content) >= BATCH_SIZE:
        print("BATCH FULL..WRITING FILES...")
        content_total = map(lambda x: x["file_content"], processed_batch_file_content)
        strf = '\n'.join(content_total)

        all_files = os.listdir("ap_nuclear/")
        text = filter(lambda x: x[0:4] == "ap99", all_files)
        files = list(text)
        i = len(files) + 1
        filename = "ap99" + str(i / 1000).split(".")[1]
        if filename in files:
            raise AttributeError("file-overiting aborted")
        with open("ap_nuclear/" + filename, 'w', encoding="utf-8") as newf:
            newf.write(strf)

        with open("ap_nuclear/html/" + filename + ".json", 'w', encoding="utf-8") as fj:
            json.dump(processed_batch_html, fj)
        processed_batch_file_content = []
        processed_batch_html = {}


# throws error if:
# url is pdf
# head-response fails
# language is not english
# GET request fails
# url is pdf
# url is pdf
def process_url_and_store(score_tuple, domain_last_request):
    # PLACE TO DECIDE IF URL IS BAD OR NOT..IF ITS BAD THROW EXCEPTION AND MOVE ON TO NEXT URL IN QUEUE
    global batch_queue_i
    url = score_tuple[1]
    if url.endswith("pdf"):
        raise AttributeError("pdf-doc")
    can_url = cannonical(url)
    print("\nProcessing url", can_url, batch_queue_i)
    batch_queue_i += 1
    header = get_HEAD_response(can_url)  # throws
    if "Content-language" in header:
        if header["Content-language"].lower().count("en") == 0:
            raise AttributeError("Non-English Language")
    if "Content-Type" in header:
        if header["Content-Type"].lower().count("html") == 0:
            raise AttributeError("Non-html Page")
    r = get_GET_response(can_url)  # throws
    domain_last_request[get_domain(can_url)] = time.time()  # update domain latest request time
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    txt = get_text(soup)

    # check if text.relevance(topic)> threshold if not then BAD PAGE DONT PROCEED
    # use text.relevance(topic) as a score

    text_relevant_factor = get_relevance_factor(txt)
    if text_relevant_factor == 0:
        raise AttributeError("Non-Relevant Page")

    tit = soup.title
    if tit is None:
        title = ""
    else:
        title = tit.string

    store_docs(can_url, title, txt, header, html_doc)
    stored_urls.add(url)

    # PROCESSING OUTGOING LINKS
    print("fetching anf verifying outgoing links", can_url)
    outgoing_links = get_exact_outgoing_links(soup, can_url, "adblock_rules", "whitelist_domains")

    positive_score_this_page = abs(score_tuple[0])
    wave_num_this_page = score_tuple[3]

    global processing_batch_urls
    print("Analyzing outgoing links", can_url)

    for linkObj in outgoing_links:
        canolink = linkObj["href"]
        if canolink in stored_urls:
            continue
        title = linkObj["title"]
        link_text = linkObj["link_text"]
        url_relevant_count = max(get_relevance_count(title), get_relevance_count(link_text))  # 0-16

        if canolink in fib_Hash:
            node_address = fib_Hash[canolink]
            tup = node_address.key
            fibheap.delete(node_address)  # removed from heap

            oldscore_positive = abs(tup[0])
            newscore = oldscore_positive + positive_score_this_page * text_relevant_factor
            new_tup = (newscore * -1, tup[1], tup[2] + 1, tup[3])
            new_node = fheappush(fibheap, new_tup)

            fib_Hash[canolink] = new_node

        elif canolink in processing_batch_urls:
            node_address = processing_batch_urls[canolink]
            tup = node_address.key
            oldscore_positive = abs(tup[0])
            newscore = oldscore_positive + positive_score_this_page * text_relevant_factor
            new_tup = (newscore * -1, tup[1], tup[2] + 1, tup[3])
            node_address.key = new_tup

        else:  # NEW LINK
            rank = 500000
            olink_domain = get_domain(canolink)
            if olink_domain in whitelist_domains:
                rank = int(whitelist_domains[olink_domain])
            else:
                if "www." + olink_domain in whitelist_domains:
                    rank = int(whitelist_domains["www." + olink_domain])

            olink_rank_score = (100 - rank / 10000)
            olink_wave_num = wave_num_this_page + 1
            olink_referScore = positive_score_this_page * text_relevant_factor
            totalscore = olink_rank_score + olink_referScore + url_relevant_count - olink_wave_num * 0.4
            olink_scoretuple = (-1 * totalscore, canolink, 1, olink_wave_num)
            new_node = fheappush(fibheap, olink_scoretuple)
            fib_Hash[canolink] = new_node
    n = fibheap.num_nodes
    print("fib-size", n)
    o_hrefs = list(map(lambda x: x["href"], outgoing_links))
    main_str = can_url + " " + " ".join(o_hrefs) + "\n"
    print("writing to linkgraph", len(o_hrefs))
    f_linkgraph.write(main_str)


batch_queue_i = 0


def process_batch():
    print("processing batch..")
    global processing_batch_queue
    global batch_queue_i
    batch_queue_i = 0
    domain_last_request = {}
    while not processing_batch_queue.empty():
        x_Node = processing_batch_queue.get()  # (-10,'url',12,3)
        tup = x_Node.key
        url = tup[1]
        domain = get_domain(url)
        if domain in domain_last_request:
            t = domain_last_request[domain]
            if time.time() - t > 1:
                try:
                    process_url_and_store(tup, domain_last_request)
                except Exception as et:
                    traceback.print_exc(file=sys.stdout)
                    continue  # BAD URL
                    # automatically updates time in hash
            else:
                processing_batch_queue.put(x_Node)
        else:
            try:
                process_url_and_store(tup, domain_last_request)
            except Exception as et:
                traceback.print_exc(file=sys.stdout)
                continue
                # automatically updates time in hash


# Initial seeding
def inital_seed():
    print("pushing seeds..")
    for surl in seed_urls:
        c = cannonical(surl)
        a = fheappush(fibheap, (-10, c, 0, 0))
        fib_Hash[c] = a


def dequeue_batch():
    n = fibheap.num_nodes
    dsize = min(n, BATCH_SIZE)
    i = 0
    print("dequing batch.. " + str(i))
    global processing_batch_queue
    processing_batch_queue = queue.Queue()
    global processing_batch_urls
    processing_batch_urls = {}
    while i < dsize:
        x_Node = fibheap.extract_min()  # removed from fibheap
        processing_batch_queue.put(x_Node)
        url = x_Node.key[1]
        processing_batch_urls[url] = x_Node
        del fib_Hash[url]  # removed from hash
        i += 1
    process_batch()

inital_seed()

while (len(stored_urls) < 90000):
    dequeue_batch()

# url = "http://en.wikipedia.org/wiki/Lists_of_nuclear_disasters_and_radioactive_incidents"
# url = "https://www.bbc.com/"
# print(get_domain(url))
# url = cannonical(url)
# r = requests.get(url)
# html_doc = r.text
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# f = open("test_links2.txt", 'w')
# str1 = get_exact_outgoing_links(soup, url, adblock_rules)
# str2 = ""
# for s in str1:
#     str2 += s["href"] + " " + s["title"] + " " + s["link_text"] + "\n"
# f.write(str2)
# a = 2
