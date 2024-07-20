# Criando um a janela no custom tkInter
from customtkinter import *
import os

def funOla():
    print('Olá mundo')
    CTkLabel(janelinha, text= 'Ola Mundo', text_color= '#000', bg_color='#bf34d1').pack(padx = 50, pady = 50)

def novJan():
    janela2 = CTk()
    janela2.title('Janela 2')
    janela2.geometry('800x600')
    CTkLabel(janela2, text= 'Nova Janela', text_color= '#B2BEBF', bg_color='#434f97').pack(padx = 80, pady = 50)
    janela2.mainloop()
    os.system('cls')
    
janelinha = CTk()

# janelinha.minsize(width= 1000, height= 600)
# janelinha.maxsize(width=1920, height=1080)
# janelinha.resizable (width=false, height = false)

#3B3936
#B2BEBF
#889C9B
#486966

janelinha.geometry('1200x720')

janelinha.title('Janela 1')
# btnOla = CTkButton(janelinha, text='Botão 1', command = funOla,fg_color= '#BD2A2E', hover_color= '#15d3b3', border_color='#000', border_width= 1)

# btnNovaJanela = CTkButton(janelinha, text='Nova Janela', command = novJan)
# btnNovaJanela.place(x = 50, y = 50)
# btnOla.pack(padx = 50, pady = 50)

frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Morango', 'Melancia', 'Abacaxi', 'Laranja', 'Limão', 'Manga']
precos = ['R$2,00','R$2,00','R$2,00','R$2,00','R$2,00','R$2,00','R$2,00','R$2,00','R$2,00']



aba =  CTkTabview(janelinha, width = 1000, height = 600)
aba.pack(padx = 50, pady = 50)
aba.add('Produtos')
aba.add('Preços')
aba.add('Promoções')
aba.tab('Produtos').columnconfigure(0, weight = 1)
aba.tab('Preços').columnconfigure(0, weight = 1)
aba.tab('Promoções').columnconfigure(0, weight = 1)

CTkLabel(aba.tab('Produtos'), text= frutas, text_color= '#B2BEBF', bg_color='#BD2A2E').pack(padx = 80, pady = 50)
CTkLabel(aba.tab('Preços'), text= precos, text_color= '#B2BEBF', bg_color='#BD2A2E').pack(padx = 80, pady = 50)
CTkLabel(aba.tab('Promoções'), text= 'Promoções', text_color= '#B2BEBF', bg_color='#BD2A2E').pack(padx = 80, pady = 50)


janelinha.mainloop()
os.system('cls')
