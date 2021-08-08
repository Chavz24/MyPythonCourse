import requests, bs4, webbrowser

web_site=open('ejemplo.html')
ejemplo_bs4=bs4.BeautifulSoup(web_site,'html.parser')

ele_web=ejemplo_bs4.select('p')
ele_web2=ejemplo_bs4.select('a')

num=0
# for i in ele_web:
#     print(num, ' ',i)
#     num+=1

# print(ele_web2[0].get('href'))


url=(str(ele_web2[0].get('href')))
#url=''.join(url)
print(url)

webbrowser.open(str(url))
# print(ele_web[1].getText())
# print(ele_web[2].getText())

