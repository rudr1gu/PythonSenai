from customtkinter import *
import os

jan = CTk()
jan.title('Exemplo 02')
jan.geometry('800x600')

frameTeste = CTkScrollableFrame(jan, label_text= 'Lista de Carros', width= 400, height= 400)

caixinha = CTkTextbox(frameTeste, width= 200, height= 30)
caixinha.pack()
caixinha.insert('1.0', 'Digite algo aqui')

carros = ['fusca', 'brasilia', 'chevette', 'opala', 'corcel', 'maverick', 'landau', 'galaxie', 'kombi', 'variant']

frameTeste.pack(padx = 10, pady = 10)

for carro in carros:
    CTkLabel(frameTeste, text= carro, text_color= '#000', bg_color='#BD2A2E').pack(padx = 2, pady = 2)

def setLabel():
    print(caixinha.get('1.0', 'end'))
    CTkLabel(frameTeste, text= caixinha.get('1.0', 'end'), text_color= '#000', bg_color='#BD2A2E').pack(padx = 2, pady = 2)


btn = CTkButton(jan, text='Enviar', command = setLabel)
btn.pack()

jan.mainloop()
os.system('cls')
