from customtkinter import *

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def funcMeses():
    print('ola')

jan = CTk()
jan.title('Exemplo 03')
jan.geometry('800x600')

mes = CTkOptionMenu(jan, values=meses, command= funcMeses)
mes.pack()


jan.mainloop()