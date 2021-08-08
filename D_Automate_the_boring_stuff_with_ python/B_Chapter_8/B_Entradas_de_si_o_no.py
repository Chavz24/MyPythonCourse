import  pyinputplus as pyip

# hace la misma pregunta al usuario

while True:

    promt='Quieres Saber como mantener a un idiota ocupado por horas?\n'
    respu=['ok','seguro','s',]
    resp=pyip.inputYesNo(promt,yesVal='si',noVal='no' )
    if resp=='no':
        break