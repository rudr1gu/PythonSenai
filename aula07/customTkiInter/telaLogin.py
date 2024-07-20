from customtkinter import *
import os

jan = CTk()
jan.title('Login')
jan.geometry('800x600')

CTkLabel(jan, text= 'Nome do usuario', text_color= '#fff', bg_color='#486966', width=200, corner_radius= 5).pack(padx = 2, pady = 2)
login = CTkEntry(jan, width= 200)
login.pack()

CTkLabel(jan, text= 'Senha', text_color= '#fff', bg_color='#486966', width=200, corner_radius=5).pack(padx = 2, pady = 2)
senha = CTkEntry(jan, width= 200)
senha.pack()

def logar():
    print(login.get())
    print(senha.get())
    if login.get() == 'admin' and senha.get() == 'admin':
        print('Logado')
        CTkLabel(jan, text= 'Logado', text_color= '#fff', bg_color='#486966').pack(padx = 2, pady = 2)
    else:
        print('Login ou senha incorretos')
        CTkLabel(jan, text= 'Login ou senha incorretos', text_color= '#fff', bg_color='#486966').pack(padx = 2, pady = 2)

btn = CTkButton(jan, text='Logar', command = logar)
btn.pack()

jan.mainloop()
os.system('cls')