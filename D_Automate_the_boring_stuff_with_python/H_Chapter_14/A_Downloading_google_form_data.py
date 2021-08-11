"""Este programa cra una lista con las direciones de email que estan dentro de un
    google spreadsheet"""
#os.chdir('C:/Users/migue/PycharmProjects/MyPythonCourse/D_Automate_the_boring_stuff_with_python/H_Chapter_14')
import ezsheets,re

ss=ezsheets.Spreadsheet('Responses')

email_regex=re.compile(r'''(^[A-Za-z0-9._$#/-]+
@
[A-Za-z0-9.-]+
(\.[A-Za-z]{2,4})
)''',re.VERBOSE)

ss.refresh()
sheet=ss[0]
email_list=[]

for rows in sheet:
    for text in rows:
        emails=email_regex.search(text)
        if emails==None:
            continue
        email_list.append(emails.group())

print(email_list)
