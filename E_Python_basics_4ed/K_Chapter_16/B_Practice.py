"""Review Exercises 16.1"""

import re
from urllib.request import urlopen

# Write a script that grabs the full HTML from the page
# http://olympus.realpython.org/profiles/dionysus.

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode('utf-8')
# print(html)

# Use the string .find() method to display the text following “Name:”
# and “Favorite Color:” (not including any leading spaces or trailing
# HTML tags that might appear on the same line)

# First match

start_tag1, start_tag2 = "Name:", "Favorite Color:"
end_tag1, end_tag2 = "</h2>", "</center>"

start_index1 = html.find(start_tag1) + len(start_tag1)
end_index1 = html.find(end_tag1)

start_index2 = html.find(start_tag2) + len(start_tag2)
end_index2 = html.find(end_tag2)

name = html[start_index1:end_index1].strip()
favorite_color = html[start_index2:end_index2].strip()

print(name, favorite_color, sep="\n")

# Repeat the previous exercise using regular expressions. The end
# of each pattern should be a “<” (the start of an HTML tag) or a
# newline character, and you should remove any extra spaces or newline
# characters from the resulting text using the string .strip() method.

pattern1 = "name:.*?<"
pattern2 = "favorite color:.*?\n"

results1 = re.search(pattern1, html, re.IGNORECASE)
results2 = re.search(pattern2, html, re.IGNORECASE)
sentence1 = results1.group()
sentence2=results2.group()

name = re.sub(".*?:", "", sentence1).strip().strip("<")
color=re.sub(".*?:","",sentence2).strip().strip("\n")

print(name)
print(color)
print(name)
