import webbrowser as wb
import pyautogui as pg
import time
import keyboard as kb

wb.open('https://www.google.com.br')
time.sleep(2)
pg.write('One Piece')
pg.press('enter')
time.sleep(2)
# pg.click(500, 500)
# posImg = pg.locateCenterOnScreen(r'A:\Prof. Deyvison Alves\Prof. Leonardo Gabriel\Antigas\Framework Sabado\Rodrigo Santos\Aula08\imgs\img.png')
pg.click(300,200)
time.sleep(2)
#pegar imagem e copiar imagem
pg.click(500,400)
time.sleep(2)