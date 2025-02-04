from urllib.parse import urljoin, urlparse

import urllib3.request
import urlcanon

import requests

wiki_domain = "en.wikipedia.org"

# lowercase only
wiki_stop_words = ["action=edit", "mobile", "cookie_statement", "wikiproject", "wikipedia:cleanup",
                   "Wikipedia:Stand-alone", "oldid", "Help:Category", "wiki/Special", "action=info", "title=Special",
                   "Wikipedia:General disclaimer", "wikipedia.org/w/index.php", "creativecommons",
                   "wiki/Special", "wiki/Portal", "wiki/Help", "wiki/Template", "wiki/Category", "wiki/Talk",
                   "wiki/Main_Page",
                   "wiki/Wikipedia", "wikimedia",
                   "mediawiki"]

common_url_stop_words = ["cookie","books.google","video", "contact-us", "donate","pubmed", "terms-of-use", "privacy-policy", "email", "javascript"]


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def isMostlyEnglish_text(test_lines):
    txt = " ".join(test_lines)
    total_words = 0
    english_words = 0
    for w in txt.split():
        total_words += 1
        if isEnglish(w):
            english_words += 1
    if english_words / total_words < 0.5:
        return False
    return True


def isMostlyEnglishLinkText(linkText):
    l = linkText.strip()
    if l == "":
        return False
    chars = list(l)
    total_words = 0
    english_words = 0
    for c in chars:
        total_words += 1
        if isEnglish(c):
            english_words += 1
    if english_words / total_words < 0.7:
        return False
    return True


def get_text(soup):
    try:
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.decompose()  # rip it out
        # get text
        body = soup.body
        if body is not None:
            text = body.text
        else:
            text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        i = 0
        lines = []
        for line in text.splitlines():
            if line:
                i += 1
                lines.append(line.strip())
        n = len(lines)
        range = min(int(n / 4), 6)
        s = int(n / 2) - range
        e = int(n / 2) + range
        test_lines = lines[s:e]
        if not isMostlyEnglish_text(test_lines):
            raise AttributeError("Non English Page")
        text = '\n'.join(lines)
        return text
    except:
        raise FileNotFoundError("BAD URL!")


def cannonical(url_string="http://///EXAMPLE.com:80/foo/../bar#ghg"):
    x = url_string.find('#')
    if x != -1:
        url_string = url_string[:x]
    url_obj = urlcanon.parse_url(url_string)
    urlcanon.whatwg(url_obj)
    return str(url_string)


def get_domain(url):
    obj = urlparse(url)
    dom=obj.netloc
    if dom.startswith("www"):
        dom=dom[4:]
    return dom
    # info = get_tld(url, as_object=True)
    # return info.fld


# gets absolute outgoing urls:
#   --non-pdfs
#   --non-self-links
#   --absolute links
#   --blocks ads
def isgoodText(title, domain):
    title = str(title).lower()
    if title.strip() == '':
        return False
    swlist = common_url_stop_words
    if domain == "en.wikipedia.org":
        swlist += wiki_stop_words
    for sw in set(swlist):
        if sw.lower() in title:
            return False
    if not isMostlyEnglishLinkText(title):
        return False
    return True


def get_exact_outgoing_links(soup_obj, base_url, rules, whitelist_domains):
    li = []
    counted_hrefs = set()
    for link in soup_obj.find_all('a'):
        href = link.get("href")
        if not href:
            continue
        href = href.strip()

        if href == '':
            continue

        if not href.startswith("http"):
            joined_url = urljoin(base_url, href)
            href = cannonical(joined_url)
        else:
            href = cannonical(href)

        # href is complete
        if href == cannonical(base_url).strip():  # self-outgoing link
            continue
        if href in counted_hrefs:
            continue
        else:
            counted_hrefs.add(href)

        if href.endswith("pdf") or href.endswith("jpg") or href.endswith("png") or href.endswith("svg"):
            continue

        domain = get_domain(href)
        if "wikipedia" in domain and domain != wiki_domain:
            continue  # non-english domain
        title = link.get("title")
        if title:
            if not isgoodText(title, domain):
                continue

        link_text = link.string
        if link_text:
            if not isgoodText(link_text, domain):
                continue

        if not isgoodText(href, domain):
            continue

        if domain not in whitelist_domains and "www."+domain not in whitelist_domains:
            # Check if Ad
            print("checking for ad..", domain, href,"title",title,"link_text",link_text)
            if rules.should_block(href):
                print("blocked")
                continue

        # NOW TESTS PASSED
        if title or link_text:
            li.append({"href": href, "title": title or "", "link_text": link_text or ""})
    return li


def get_GET_response(url):
    r = requests.get(url, timeout=5)
    if r.status_code in range(400, 600):
        raise EOFError("Error response from page" + r.status_code)
    else:
        return r


def get_HEAD_response(url):
    r = requests.head(url, timeout=5)
    if r.status_code in range(400, 600):
        raise EOFError("Error response from page" + r.status_code)
    else:
        return r.headers

# print(cannonical(
#     "https://en.wikipedia.org/wiki/Lists_of_nuclear_disasters_and_radioactive_incidents#/media/File:Sl-1-ineel81-3966.jpg"))
# # st= time.time()
# print("here")
# print(isAd("http://www.g.com&adnum=4"))
# print(isAd("http://www.g.com&adnum=5"))
# print(isAd("https://en.wikipedia.org/wiki/Operation_Hardtack_I"))
# print(time.time()-st)
# def get_text(link):
