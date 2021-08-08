#!python3

import webbrowser,sys,bs4,requests


print('Searching...')

res=requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

search_results=bs4.BeautifulSoup(res.text, 'html.parser')

links_ele=search_results.select('.package-snippet')

num_taps_to_open=min(5,len(links_ele))
for i in range (num_taps_to_open):
    url_to_open='https://pypi.org/search/?q='+links_ele[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)