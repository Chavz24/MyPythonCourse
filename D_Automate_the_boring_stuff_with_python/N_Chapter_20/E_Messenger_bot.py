"""Este bot esta se usa paa mandar mensajes usando  google hangouts"""

import webbrowser,pyautogui

# Datos
url='https://hangouts.google.com/'
user='ramdom_user@gmail.com'
password='pass_here'
lista_amigos=['friend\'s name/s here']
mensaje="mesaje_here"

webbrowser.open(url)
pyautogui.sleep(3)

def handle_pop_up():
    pyautogui.sleep(3)
    if pyautogui.locateOnScreen('ED_Nunca.PNG') != None:
        pyautogui.click('ED_Nunca.PNG')
    else:
        pass

def mesage_sender():
    for name in lista_amigos:

        if pyautogui.locateOnScreen('EF_Nueva_Conversacion.PNG') != None:
            pyautogui.click('EF_Nueva_Conversacion.PNG')
            pyautogui.sleep(2)
            pyautogui.write(name, 0.20)
            pyautogui.moveTo(302, 724, 1)
            pyautogui.press('down')
            pyautogui.press('\n')
            pyautogui.sleep(2)
            # Determinando si el contacto esta en linea
            if pyautogui.locateOnScreen('EG_Online.PNG') != None or pyautogui.locateOnScreen('EG_Online1.PNG') != None:
                pyautogui.sleep(1)
                pyautogui.write(mensaje, 0.10)
                pyautogui.press('\n')
                pyautogui.sleep(1)
                pyautogui.click(1841, 284)
            else:  # Contacto offline
                print(f'{name.capitalize()} esta offline.')
                pyautogui.click(1841, 284)
                # pyautogui.click('EH_Cerrar_Chat.PNG')

    pyautogui.sleep(2)
    pyautogui.click(1828, 193)
    pyautogui.sleep(2)
    pyautogui.click('EI_Cerrar_sesion.PNG')

def login_session():
    """Esta funcion te logea en la cuenta por primera vez"""
    if pyautogui.locateOnScreen('EB_Correo.PNG') and pyautogui.locateOnScreen('EC_Siguente.PNG')!=None:

        # Logeandome en la cuenta
        pyautogui.sleep(2)
        pyautogui.write(user,0.10)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.write(password,0.20)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        handle_pop_up()

    else:
        raise 'Se necesita un relogin.'

def relogin_session():
    pyautogui.sleep(2)
    if pyautogui.locateOnScreen('EE_User.PNG') != None:
        pyautogui.click('EE_User.PNG')
        pyautogui.sleep(2)
        pyautogui.write(user, 0.10)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.write(password, 0.20)
        pyautogui.sleep(1)
        pyautogui.press('enter')

def vericador_sesion_iniciada():
    if pyautogui.locateOnScreen('EF_Nueva_Conversacion.PNG') != None:
        pyautogui.sleep(2)
        pyautogui.click(1828, 193)
        pyautogui.sleep(2)
        pyautogui.click('EI_Cerrar_sesion.PNG')
        return 'Hay una sesion iniciada'
    return None

def pagina_principal():
    """Esta funcion  inicia sesion desde la pagina principal"""
    pyautogui.sleep(3)
    ven = pyautogui.getActiveWindow()
    pyautogui.moveTo(ven.centerx,ven.centery,0.5)
    pyautogui.sleep(0.5)
    pyautogui.scroll(-500)
    pyautogui.sleep(0.5)
    pyautogui.scroll(500)
    # Entrando al inicio de seccion
    coords = pyautogui.locateOnScreen('EA_Inicio.PNG')
    pyautogui.moveTo(coords.left, coords.top, 0.5)
    pyautogui.click(coords.left, coords.top)
    pyautogui.sleep(3)
    try:
        login_session()
    except:
        relogin_session()

print('Verificando si hay una sesion iniciada...')

if vericador_sesion_iniciada()==None:
    print('No hay sesion iniciada.')
    pagina_principal()
    pyautogui.sleep(3)
    mesage_sender()
else:
    webbrowser.open(url)
    pyautogui.sleep(3)
    pagina_principal()
    pyautogui.sleep(3)
    mesage_sender()
