from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/aphrodite"
html_page = urlopen(url)

html_text = html_page.read().decode('utf-8')
# print(html_text)
start_tag = "<title>"
end_tag = "</title>"

star_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

# print(html_text[star_index:end_index])

# the "<title >" has a space  so it does not match

url = "http://olympus.realpython.org/profiles/poseidon"
html_page = urlopen(url)

html_text = html_page.read().decode('utf-8')
# print(html_text)
start_tag = "<title>"
end_tag = "</title>"

star_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

# print(html_text[star_index:end_index])

# To solve this use regex

url = "http://olympus.realpython.org/profiles/poseidon"
html_page = urlopen(url)

html_text = html_page.read().decode('utf-8')
# print(html_text)

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html_text, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)
print(title)




# More html parsing with regex

url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)

html_text = html_page.read().decode('utf-8')
print(html_text)


pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html_text, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)
print(title)

