import requests
from bs4 import BeautifulSoup

import langid

from crawler_lib import get_HEAD_response, get_GET_response, get_domain

h = get_HEAD_response("https://ca.wikipedia.org/wiki/Vulnerabilitat_de_les_centrals_nuclears_als_atacs Vulnerabilitat de les centrals nuclears als atacs – Catalan Català")
# h= get_HEAD_response("https://upload.wikimedia.org/wikipedia/commons/4/40/Sl-1-ineel81-3966.jpg")
if "Content-Type" in h:
    print(h["Content-Type"].lower().count("html")!=0)
print(h)
c = get_GET_response("https://en.wikipedia.org/w/index.php?title=Lists_of_nuclear_disasters_and_radioactive_incidents&action=edit&section=1")
# c = get_GET_response("https://www.bbc.com/hindi/science-51695982")
# print(c)
# print(len(c))
print(get_domain("https://ca.wikipedia.org/wiki/Vulnerabilitat_de_les_centrals_nuclears_als_atacs"))
a=(1,2,3)