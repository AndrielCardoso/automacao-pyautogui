import pyautogui
import time

pyautogui.alert('O código vai começar, por favor não utilize o computador.')

#  Abrir o explorador de arquivos
pyautogui.hotkey('win','d')
pyautogui.click(x=182, y=142, clicks=2, interval=0.03, button='left')
time.sleep(0.5)
pyautogui.hotkey('winleft','up')
time.sleep(0.5)

# Clicar na pasta C# studies

pyautogui.click(x=249, y=341, clicks=2, interval=0.03, button='left')

# Abrir o google chrome

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('alt','tab')
time.sleep(0.5)
pyautogui.hotkey('winleft','up')
time.sleep(0.3)

# Digitar github
pyautogui.write('https://github.com/AndrielCardoso')
time.sleep(0.2)
pyautogui.press('enter')
time.sleep(1.5)

# Abrir repositório no github

pyautogui.click(x=821, y=251, clicks=1, interval=0.03, button='left')
time.sleep(2)

# Abrir pasta dentro do repositório

pyautogui.click(x=676, y=396, clicks=1, interval=0.03, button='left')
time.sleep(1.5)
pyautogui.click(x=1115, y=382, clicks=1, interval=0.03, button='left')
time.sleep(0.5)
pyautogui.click(x=1044, y=460, clicks=1, interval=0.03, button='left')
time.sleep(0.5)

# Colocar o arquivo dentro e fazer upload

pyautogui.hotkey('alt','tab')
time.sleep(0.5)
pyautogui.moveTo(233, 130)
time.sleep(0.5)
pyautogui.mouseDown()
time.sleep(0.5)
pyautogui.moveTo(813, 604)
time.sleep(0.5)
pyautogui.hotkey('alt','tab')
pyautogui.mouseUp()
time.sleep(0.5)
pyautogui.click(x=403, y=968, clicks=1, interval=0.03, button='left')
pyautogui.write('Teste')
time.sleep(0.5)
pyautogui.click(x=27, y=652, clicks=1, interval=0.03, button='left')
time.sleep(0.5)
pyautogui.moveTo(1909, 470)
time.sleep(0.5)
pyautogui.mouseDown()
pyautogui.moveTo(1914, 811)
pyautogui.mouseUp()
time.sleep(0.5)
pyautogui.click(x=360, y=861, clicks=1, interval=0.03, button='left')

