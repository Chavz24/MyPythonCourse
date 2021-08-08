#crea un programa que pida nombre,direcciony telefono por teclado. El programa debe almacenar estos
#datos en una lista y mostrar esos datos en consola.

print("*"*8, 'Lista datos personalees',"*"*8,'\n')

datos_persona=[]

nombre_persona=input('Ingrese el nombre de la persona: ')
dirrecion_persona=input('Ingrese la dirrecion de la persona: ')
telefono_persona=input('Ingrese el telefono de la persona: ')

datos_persona.append(nombre_persona)
datos_persona.append(dirrecion_persona)
datos_persona.append(telefono_persona)

print(f'''Estos son los datos de la persona,
Nombre: {datos_persona[0].upper()}
direccion: {datos_persona[1].upper()}
telefono: {datos_persona[2]} ''')

