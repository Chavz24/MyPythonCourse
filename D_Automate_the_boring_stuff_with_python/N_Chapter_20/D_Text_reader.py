"""Este program abre un documento capia su contenido y lo pega en la consola"""

import subprocess, pyautogui, pyperclip
from pygetwindow import PyGetWindowException

# Abre el archivo de texto
subprocess.Popen(['Inserte_.exe_aqui', 'Inserte_ubicacion_del_archivo_aqui_(opcinal)'])

pyautogui.sleep(0.07)  # Espera hasta que se habra el archivo
try:
    ven = pyautogui.getWindowsWithTitle('Inserte_titulo_app_aqui.')
    notepad = ven[0]
    notepad.activate()
    notepad.maximize()
    if notepad.isMaximized:
        center = notepad.center  # Ubica el centro de la ventana del notepad
        pyautogui.click(center.x, center.y)
        pyautogui.sleep(0.07)
        pyautogui.hotkey('ctrl', 'e')
        pyautogui.sleep(0.07)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.sleep(0.07)
        notepad.close()
    else:
        print('Se ha producido un error')
except PyGetWindowException:
    print('cant do')

text = pyperclip.paste()

print(text)
