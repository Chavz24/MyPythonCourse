import pyautogui

formData = [{'name': 'James Bond', 'fear': 'M', 'source': 'wand',
             'robocop': 4, 'comments': 'A martini. Shaken, not stirred.'},
            {'name': 'GoldFinger', 'fear': 'Bond', 'source': 'amulet', 'robocop': 4,
             'comments': 'No Mr. Bond I expect you to die'},
            {'name': 'Plenty O\'tool', 'fear': 'puppets', 'source': 'crystal ball',
             'robocop': 1, 'comments': 'I\'m Plenty.'},
            {'name': 'Mr. Kil', 'fear': 'ED-209', 'source': 'money',
             'robocop': 5, 'comments': 'Now that\'s a name to die for.'},]

for person in formData:
    print('The program will start in 5 seconds...')
    print('You can quit this program by draging the mouse to any conner of the screen')
    print('Asegurate de que el browser este en la pagina de la forma a llenar')
    pyautogui.sleep(5)

    print(f'Entering {person["name"]} info...')
    pyautogui.write(['\t', '\t'])

    # Campo del nombre
    pyautogui.write(person['name'] + '\t', 0.25)

    # Campo mayor miedo
    pyautogui.write(person['fear'] + '\t', 0.25)

    pyautogui.scroll(-500)
    # Campo drop down box

    if person['source'] == 'wand':
        pyautogui.write(['down', '\n', '\t'],interval=0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', '\n', '\t'],interval=0.5)
    elif person['source']=='crystal ball':
        pyautogui.write(['down', 'down','down', '\n', '\t'],interval=0.5)
    elif person['source']=='money':
        pyautogui.write(['down', 'down', 'down','down', '\n', '\t'],interval=0.5)

    #Campo 'robocop'
    if person['robocop']==1:
         pyautogui.write([' ','\t','\t'],0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right','\t','\t'],0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right','right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
         pyautogui.write(['right', 'right','right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right','right', '\t', '\t'], 0.5)

    pyautogui.scroll(-500)

    #Comentarios
    pyautogui.write(person['comments']+'\t',0.25)

    pyautogui.sleep(0.5)
    #Sumit la solicitud
    pyautogui.press('enter')
    print('Solicitud completada')
    pyautogui.sleep(5)
    #Llenar otra solicitud
    pyautogui.click(554,392,duration=0.5)
