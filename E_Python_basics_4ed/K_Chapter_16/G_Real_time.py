import time
import mechanicalsoup

browser = mechanicalsoup.Browser()
for i in range(4):
    url = "http://olympus.realpython.org/dice"
    page = browser.get(url)

    tag = page.soup.select("h2")[0]
    print(f"Dice current number is: {tag.text}.")

    if i < 3:
        time.sleep(2)

