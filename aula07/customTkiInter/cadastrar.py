from customtkinter import *

produtos = {'Banana':{'valor': 2.00, 'quantidade': 10},
            'Maçã':{'valor': 2.50, 'quantidade': 10},
            'Pera':{'valor': 3.00, 'quantidade': 10},
            'Uva':{'valor': 4.00, 'quantidade': 10},
            'Morango':{'valor': 5.00, 'quantidade': 10},
            'Melancia':{'valor': 6.00, 'quantidade': 10},
            'Abacaxi':{'valor': 7.00, 'quantidade': 10},
            'Laranja':{'valor': 8.00, 'quantidade': 10},
            'Limão':{'valor': 9.00, 'quantidade': 10},
            'Manga':{'valor': 10.00, 'quantidade': 10}
            }

jan = CTk()
jan.title('Cadastro')
jan.geometry('800x600')

aba =  CTkTabview(jan, width = 1000, height = 600)
aba.pack(padx = 50, pady = 50)
aba.add('Cadastrar')
aba.tab('Cadastrar').columnconfigure(0, weight = 1)

def cadastrar():
    print(nome.get())
    print(valor.get())
    print(quantidade.get())
    produtos[nome.get()] = {'valor': valor.get(), 'quantidade': quantidade.get()}
    print(produtos)

CTkLabel(aba.tab('Cadastrar'), text= 'Nome do Produto', text_color= '#fff', bg_color='#486966', width=200).pack(padx = 2, pady = 2)
nome = CTkEntry(aba.tab('Cadastrar'), width= 200)
nome.pack()

CTkLabel(aba.tab('Cadastrar'), text= 'Valor do Produto', text_color= '#fff', bg_color='#486966', width=200).pack(padx = 2, pady = 2)
valor = CTkEntry(aba.tab('Cadastrar'), width= 200)
valor.pack()

CTkLabel(aba.tab('Cadastrar'), text= 'Quantidade do Produto', text_color= '#fff', bg_color='#486966', width=200).pack(padx = 2, pady = 2)
quantidade = CTkEntry(aba.tab('Cadastrar'), width= 200)
quantidade.pack()

btn = CTkButton(aba.tab('Cadastrar'), text='Cadastrar', command = cadastrar)
btn.pack()

aba.add('Remover')
aba.tab('Remover').columnconfigure(0, weight = 1)

def remover():
    print(nomeRemover.get())
    produtos.pop(nomeRemover.get())
    print(produtos)

CTkLabel(aba.tab('Remover'), text= 'Nome do Produto', text_color= '#fff', bg_color='#486966', width=200).pack(padx = 2, pady = 2)
nomeRemover = CTkEntry(aba.tab('Remover'), width= 200)
nomeRemover.pack()

btn = CTkButton(aba.tab('Remover'), text='Remover', command = remover)
btn.pack()

aba.add('Consultar')
aba.tab('Consultar').columnconfigure(0, weight = 1)

def consultar():
    print(nomeConsultar.get())
    CTkLabel(aba.tab('Consultar'), text= f'Produto: {nomeConsultar.get()}').pack(padx = 2, pady = 2)
    CTkLabel(aba.tab('Consultar'), text= f'Valor: {produtos[nomeConsultar.get()]["valor"]}').pack(padx = 2, pady = 2)
    CTkLabel(aba.tab('Consultar'), text= f'Quantidade: {produtos[nomeConsultar.get()]["quantidade"]}').pack(padx = 2, pady = 2)

CTkLabel(aba.tab('Consultar'), text= 'Nome do Produto', text_color= '#fff', bg_color='#486966', width=200).pack(padx = 2, pady = 2)
nomeConsultar = CTkEntry(aba.tab('Consultar'), width= 200)
nomeConsultar.pack()

btn = CTkButton(aba.tab('Consultar'), text='Consultar', command = consultar)
btn.pack()

aba.add('Listar')
aba.tab('Listar').columnconfigure(0, weight = 1)

frame = CTkScrollableFrame(aba.tab('Listar'), label_text='Lista de Produtos', width= 400, height= 150)
frame.pack(padx = 10, pady = 10)

for produto in produtos:
        CTkLabel(frame, text= f'Produto: {produto} Valor: {produtos[produto]["valor"]} Quantidade: {produtos[produto]["quantidade"]}').pack(padx = 2, pady = 2)

def atualizar():
    for produto in produtos:
        CTkLabel(frame, text= f'Produto: {produto} Valor:{produtos[produto]["valor"]} Quantidade: {produtos[produto]["quantidade"]}').pack(padx = 2, pady = 2)
    
def limpar():
    for widget in frame.winfo_children():
        widget.destroy()

btn = CTkButton(aba.tab('Listar'), text='Atualizar', command = atualizar)
btn.pack()

btnLimpar = CTkButton(aba.tab('Listar'), text='Limpar', command = limpar)
btnLimpar.pack(padx = 4, pady = 4)

aba.add('Sair')
aba.tab('Sair').columnconfigure(0, weight = 1)

def sair():
    jan.destroy()

btn = CTkButton(aba.tab('Sair'), text='Sair', command = sair)
btn.pack()

jan.mainloop()
os.system('cls')