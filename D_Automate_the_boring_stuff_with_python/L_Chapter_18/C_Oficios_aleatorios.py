import random, smtplib

#persona que van a realizar los oficios
personas_correos={'Manuel':'insert_email_here','robert':'insert_email_here'}

oficios=['Limpiar Patio','Cocinar']

oficio_aleatorio=random.choice(oficios)

tarea_previa={}#este dict se usa para llevar un record de las actividades asignadas

#conectando con el servidor de e mail
smtp_obj= smtplib.SMTP('dominio_de_mail',0)#esto es el nombre del dominio del servidor y el numero del puerto
smtp_obj.ehlo()
smtp_obj.starttls()#encriptando la coneccion.
smtp_obj.login('mi_correo','mi_contrasena')

# Recorriendo el dict de personas que van a realizar los oficios.
for nombre,correo in personas_correos.items():
    #este if verifica si la tarea actual se le asigno previamente
    if nombre in tarea_previa.keys() and tarea_previa[nombre]==[oficio_aleatorio]:
        cuerpo_email = f'Subject:Oficio de hoy.\nSaludos {nombre}, hoy te toca {oficio_aleatorio}.'
        oficio_aleatorio=random.choice(oficios)
        print(f'Enviando correo a {correo}')
        #enviando email con oficio a realizar
        email_status = smtp_obj.sendmail('mi_correo', correo, cuerpo_email)
        #verificando si el email se envio
        if email_status!={}:
            print(f'No se ha podido enviar correo a {correo}')
        oficios.remove(oficio_aleatorio)
    # en caso de que el oficio asignado no es el mismo que el previo
    else:
        cuerpo_email = f'Subject:Oficio de hoy.\nSaludos {nombre}, hoy te toca {oficio_aleatorio}.'
        print(f'Enviando correo a {correo}')
        email_status = smtp_obj.sendmail('mi_correo', correo, cuerpo_email)
        if email_status!={}:
            print(f'No se ha podido enviar correo a {correo}')
        oficios.remove(oficio_aleatorio)
    #actializa el dict de tarea previa
    tarea_previa[nombre]=[oficio_aleatorio]
    #este if evita que el program de error si la lista esta vacia.
    if len(oficios)!=0:
        oficio_aleatorio=random.choice(oficios)

smtp_obj.quit()#corta la conecion con el server del e mail