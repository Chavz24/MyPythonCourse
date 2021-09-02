"""Review Exercises 16.3"""

import mechanicalsoup

#  Use Mechanical Soup to provide the correct username “zeus” and
# password “ThunderDude” to the login page submission form
# located at http://olympus.realpython.org/login.

url = "http://olympus.realpython.org/login"
browser = mechanicalsoup.Browser()
page = browser.get(url)

login_form = page.soup.select("form")[0]

user_name = login_form.select("input")[0]
user_name["value"] = "zeus"
passwrd = login_form.select("input")[1]
passwrd["value"] = "hunderDude"

profile_page = browser.submit(form=login_form, url=page.url)
print(profile_page.url)

# Display the title of the current page to determine that you have
# been redirected to the /profiles page.

title = profile_page.soup.select("title")[0]
print(title.string)

# Use Mechanical Soup to return to login page by going “back” to the
# previous page.

page = browser.get(url)
page_title = page.soup.title.text

# Provide an incorrect username and password to the login form,
# then search the HTML of the returned webpage for the text
# “Wrong username or password!” to determine that the login
# process failed.


if profile_page.soup.text.find("Wrong username or password!") != -1:
    print("Failed Login")
