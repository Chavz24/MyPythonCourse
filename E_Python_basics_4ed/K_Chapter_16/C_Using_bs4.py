from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode("utf-8")
# print(html)
soup = BeautifulSoup(html, "html.parser")

img1, img2 = soup.find_all("img")

print(soup.find("img", src="/static/dionysus.jpg"))
