
import PyPDF2
from random import choice

#Making  a list of all the words in the text
words=open('GG_Dictionary.txt','r')
password_list=[]
for word in words:
    password_list.append(word.strip('\n'))
    password_list.append(word.lower().strip('\n'))

print(len(password_list))
#Picking a random word in the list
password=choice(password_list)
print(password)

#Encrypting the pdf with a random password
pdf_file=open('AAA_Unite.pdf','rb')
pdf_obj=PyPDF2.PdfFileReader(pdf_file)

new_pdf=PyPDF2.PdfFileWriter()

for page_num in range(pdf_obj.numPages):
    new_pdf.addPage(pdf_obj.getPage(page_num))

new_pdf.encrypt(password)
encrypted_pdf=open('GG_Unite_encrypted.pdf','wb')
new_pdf.write(encrypted_pdf)
encrypted_pdf.close()
pdf_file.close()

#Creating the decrypter

encrypted_pdf_file= open('GG_Unite_encrypted.pdf','rb')
encrypted_pdf_obj=PyPDF2.PdfFileReader(encrypted_pdf_file)

for word in password_list:
    if encrypted_pdf_obj.decrypt(word)==1:
        print(f'La contrasena es {word}')
        break


encrypted_pdf_file.close()
