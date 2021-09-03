"""Review Exercises 16.4"""

import time
import datetime as dt
import mechanicalsoup

# Repeat the example in this section to scrape the die roll result, but
# additionally include the current time of the quote as obtained from
# the webpage. This time can be taken from part of a string inside a
# <p> tag that appears shortly after the result of the roll in the webpage’s HTML.

browser = mechanicalsoup.Browser()

for i in range(4):
    url = "http://olympus.realpython.org/dice"
    page = browser.get(url)

    dice_tag = page.soup.select("h2")[0].text
    time_tag = page.soup.select("p")[1].text
    # extrating the time from the time tag
    current_time = dt.datetime.strptime(time_tag, "%B %d, %Y %H:%M:%S%p").strftime("%H:%M:%S%p")

    print(f"The dice roll is: {dice_tag}. The time is: {current_time}.")

    if i < 3:
        time.sleep(2)
