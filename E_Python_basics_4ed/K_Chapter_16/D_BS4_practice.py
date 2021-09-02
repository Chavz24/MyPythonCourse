"""Review Exercises 16.2"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Write a script that grabs the full HTML from the page
# http://olympus.realpython.org/profiles

url = "http://olympus.realpython.org/profiles"

page = urlopen(url)
html = page.read().decode("utf-8")

# Parse out a list of all the links on the page using Beautiful Soup by
# looking for HTML tags with the name a and retrieving the value
# taken on by the href attribute of each tag.

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")

pages = []
for link in links:
    new_url = url.strip("/profiles") + link["href"]
    pages.append(new_url)

# Get the HTML from each of the pages in the list by adding the full
# path to the file name, and display the text (without HTML tags) on
# each page using Beautiful Soup’s .get_text() method.

for page in pages:
    page_url = urlopen(page)
    html = page_url.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup.get_text().replace("\n", ""))
