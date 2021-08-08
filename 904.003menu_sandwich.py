#crea un program que tome la orden de sandwitch de un cliente

from pyinputplus import inputYesNo,inputMenu,inputInt

precio_pan={'Sobao':10,'Dulce':20,'De agua':5,'Pan Blanco':15}
precio_carne={'Pavo':20,'Cerdo':25,'Polo':15,'Res':30}
precio_queso={'Barrigaverde':10,'QuesoBlanco':15,'Cheddar':20}

orden_cliente=[]
precio_orden=0

opcion_pan=inputMenu(['Sobao','Dulce','De agua','Pan Blanco'],
                          prompt='Que tipo de pan desea: \n',numbered=True)
orden_cliente.append(opcion_pan)

opcion_carne=inputMenu(['Pavo','Cerdo','Pollo','Res'],
                            prompt='Que tipo de carne desea: \n', numbered=True)
orden_cliente.append(opcion_carne)
queso=inputYesNo(prompt='Desea queso: \n',yesVal='si')

if queso=='si':
    opcion_queso=inputMenu(['Barrigaverde','QuesoBlanco','Cheddar']
                                ,prompt='Que tipo de queso desea: \n', numbered=True)
    orden_cliente.append(opcion_queso)
opcion_contimento1=inputYesNo(prompt='Desea mayonesa?',yesVal='si')
opcion_contimento2=inputYesNo(prompt='Desea mostaza?',yesVal='si')
opcion_contimento3=inputYesNo(prompt='Desea Ketchup?',yesVal='si')
opcion_contimento4=inputYesNo(prompt='Desea salsa picante?',yesVal='si')

cantidad_sandwich=inputInt(prompt='Cuantos sandwich desea?:', min=1)


for ingrediente in orden_cliente:
    if ingrediente in opcion_pan:
        precio_orden+=precio_pan[ingrediente]
    elif ingrediente in opcion_carne:
        precio_orden+=precio_carne[ingrediente]
    elif ingrediente in opcion_queso:
        precio_orden+= precio_queso[ingrediente]
    else:
        continue


print('El total de su orden es: '+ str(precio_orden*cantidad_sandwich))



