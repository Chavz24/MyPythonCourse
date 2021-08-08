'''expresiones regulares. La sigueiente expresion regular busca telefonos de con el formto sig
"***-***-****"'''
import re

numeroTelefonico = re.compile(r'\d{3}-\d{3}-\d{4}')
# usando el metodo .search par buscar el regex detro de un string
miNumero = numeroTelefonico.search('Mi numero de telefono es 9999-809-707-132699999')
# print('Numero de telefono encontrado: '+miNumero.group())

# agrupando partes dentro de una expresion regular

numeroTelefonico2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')

miNumero2 = numeroTelefonico2.search('Mi numero de telefono es 809-707-1326,')

# print('Codigo de area: '+miNumero2.group(1))
# print("Telefono: "+ miNumero2.group(2))

# metodo .groups extrae los datos dentro de una tupla

# print(miNumero2.groups())
codigoArea, numeroTel = miNumero2.groups()  # asignacion multiple
# print(codigoArea)
# print(numeroTel)

# Buscando un numero del formato (***)-***-****

nuevoNumero = re.compile(r'(\(\d{3}\))\s?\d{3}-\d{4}')  # \s? significa con espacio o sin espacio
miNumero3 = nuevoNumero.search('Mi nuevo numero es (456)567-1234')
# print(miNumero3.group())

# Uso de la barra verticla (|).Se usa para hacer un matchear una de varias expresiones

v = re.compile(r'A3|B')

letra = v.search('Es A o B')
letra2 = v.search('es B o A')

# print(letra.group())
# print(letra2.group())

# tambien se puede usar la barra par especificar un prefijo

v = re.compile(r'Pan(aderia|andero|dora|cito|za)')
palabra = v.search("Pandora tiene la Panza grande")
# solo va  a imprimir Pandora, la primera coincidencia
# print(palabra.group())

# tambien se puede hacer una parte del regex opcional con el simbolo (?)

# \s? significa con espacio o sin  con codigo de area, y si tiene codico de area sin o scon espacio
# con los demas caracteres

nuevoNumero = re.compile(r'(\(\d{3}\)|\d{3})?(-)?\d{3}-\d{4}')
# con codigo de area y sin espacio entre el codigo de area y el numero principal
# miNumero3 = nuevoNumero.search('Mi nuevo numero es 456-567-1234')
# print(miNumero3.group())
# sin codigo de area
miNumero4 = nuevoNumero.search('Mi nuevo numero es 567-1234')
# print(miNumero4.group())

# el (*) matchea lo que lo preceda las veces que aparezca en el string
v = re.compile(r'Pan(aderia|andero|dora|cito|za)*')
# como el * no le importa las veces que parezca el grupo puede o no aparecer en el string
# palabra = v.search("Panaderiaaderia")
# print(palabra.group())
palabra2 = v.search("Pan")
# print(palabra2.group())


# el (+) matchea lo que lo preceda las veces que aparezca en el string
v = re.compile(r'Pan(aderia|andero|dora|cito|za)+')
# como el +  le importa las veces que parezca el grupo debe  aparecer en el string
# palabra = v.search("Panaderiaaderia")
# print(palabra.group())
# de lo contrario da error
# palabra2 = v.search("Pan")
# print(palabra2.group())

# the ,findall() method a diferencia del metodo .search, hace un match de todos los elementos
# posibles en una cadena


nuevoNumero = re.compile(r'\d{,3}?-\d{,3}-\d{,4}')

# solo regresa la primera coincidencia(.serch())
# misNumeros=nuevoNumero.search("Numero casa: 456-567-1234. Numero Cel: 678-234-678")
# print(misNumeros.group())
# regresa la primera coincidencia (.findall())
# print(nuevoNumero.findall("Numero casa: 56-567-1234 Numero Cel: 678-34-678"))

# en caso que los elementos del regex se encuentren en grupos, metodo .findall() retornara
# una lista de tuplas y cada grupo dento de la tupla es una cadena de cada elemento matcheado por el regex

# nuevoNumero = re.compile(r'(\d{,3})?-(\d{,3})-(\d{,4})')
# print(nuevoNumero.findall("Numero casa: 56-567-1234 Numero Cel: 678-34-678 , Oficina:789-908-1256"))


# El punto (.) en las expresiones regulares representa a todos los caracteres excepto una linea nueva
# newline(\n)

# este regex le dice al metodo .finall) que encuentre todos los caracteres antes de la letra (o)
allRegex = re.compile(r'.*')
# print(allRegex.search("expresiones regulares representan"))

# sis se quiere incluir newline(\n) se le debe pasar el re.DOTALL como argumento secundario a la
# funcion re.compile

# allRegex = re.compile(r'.*', re.DOTALL)
# print(allRegex.search("expresiones regulares representan\no Cel: 678-34-678\nle dice al metodo"))


# sustituyendo: para sustituir un regex con otro elemento, se utiliza el metodo .sub()
# este metodo consta de dos argumentos el primero, es el elemento el cual sustituira al regex
# y el segund es la cadena donde se va a sustituir.


# voy a usar est regex para censurar my numero d e telefono
# nuevoNumero = re.compile(r'(\d{,3})?-(\d{,3})-(\d{,4})')

# print(nuevoNumero.sub('***-***-****',"Numero casa: 56-567-1234 Numero Cel: 678-34-678 , Oficina:789-908-1256"))

# para maneajr regexes complejos conviene usar expresiones reglares que ignoren espacio y
# lineas dentro de su declaracion. Para esto se usa la funcion .reVERBOSE como segundo argumento
# dentro de la funcion re.compile

# en este ejemplo se va a crer un regex que busque numeros de telefono en un
# string y sus extensiones

buscarNuevoNumero = re.compile(r'''(
(\(\d{3}\)|\d{3})?                              #codigo area
(\s|\.|-)?                                      #separador
(\d{3})                                         #primeros tres digitos numero principal
(\s|\.|-)                                       #segundo separador
(\d{4})                                         #ultimos cuatro digitos
(\s*(ext.|x.|ext|x))?(\s*\d{,5})?)'''           # extension
, (re.VERBOSE | re.I))                          #re.VERBOSE ignora espacio en blanco
                                                #re.I ve mayusculas y minusculas por igual

print(buscarNuevoNumero.findall("Oficina:789-908-1256 ext. 2456 thelow: 239-567-3569 ext. 3456"))
p = buscarNuevoNumero.search("Oficina: (709)-908-1256X.3345 ")

print(p.group())
