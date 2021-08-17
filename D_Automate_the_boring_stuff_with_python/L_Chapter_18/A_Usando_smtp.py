import smtplib

smtp_obj= smtplib.SMTP('smtp.gmail.com',587)#esto es el nombre del dominio del servidor y el numero del puerto
smtp_obj.ehlo()
smtp_obj.starttls()#encriptando la coneccion.
smtp_obj.login('mi_correo','mi_contrasenia')
smtp_obj.sendmail('mi_correo',['Correo_destino_1','Correo_destino_2'],
                  'Subject:Prueba.\nEste es otro correo de prueba usando SMTP')
smtp_obj.quit()#desconectando del servidor.



