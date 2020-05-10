'''
Agenda mista; Tkinter com tabela
Adaptado do Denilson https://www.youtube.com/watch?v=1RjEnbLymN4


from django.db import connection

# get a cursor object from the database connection
cursor = connection.cursor()

# my_query is a string with the SQL you want executed
cursor.execute(<my_query>)

#you can fetch the next row using the cursors fetchone method
row = cursor.fetchone()

#you can also get all results by using the fetchall method
row = cursor.fetchall()

#make sure to clean up
cursor.close()





'''

import sqlite3
from tkinter import *
from random import randint

conectar = sqlite3.connect('Banquinho.db')
c = conectar.cursor()
#n_ordem = 1

janela = Tk()

txtOrdem = StringVar()
txtNome = StringVar()
txtSobrenome = StringVar()
txtTelefone = StringVar()

n_ordem= StringVar()
x_nome= StringVar()
x_sobrenome= StringVar()
n_telefone= StringVar()

n_atual = 1

def btInserir_click():
    sqltotal = 'SELECT * FROM tabelinha'
    c.execute(sqltotal)
    n_total = c.fetchall()
    quantos = len(n_total)
    n_novo = quantos + 1
    getOrdem.delete(0, END)
    getOrdem.insert(0, n_novo)

    n_ordem= getOrdem.get()
    x_nome= getNome.get()
    x_sobrenome= getSobrenome.get()
    n_telefone= getTelefone.get()

    c.execute("INSERT INTO tabelinha (ordem, nome, sobrenome, telefone) VALUES (?,?,?,?)", (n_ordem, x_nome, x_sobrenome, n_telefone))
    conectar.commit()

def btAlterar_click():
    sqltotal = 'SELECT * FROM tabelinha'
    c.execute(sqltotal)

    n_ordem = getOrdem.get()
    x_nome = getNome.get()
    x_sobrenome = getSobrenome.get()
    n_telefone = getTelefone.get()

    lb2Nome["text"] = str(x_nome)
    lb2Sobrenome["text"] = str(x_sobrenome)
    lb2Telefone["text"] = str(n_telefone)

    c.execute("UPDATE tabelinha SET ordem= ?, nome= ?, sobrenome = ?, telefone = ? WHERE ordem = ?",
              (n_ordem, x_nome, x_sobrenome, n_telefone, n_ordem))
    conectar.commit()

def btExcluir_click():
    sqltotal = 'SELECT * FROM tabelinha'
    c.execute(sqltotal)
    n_ordem = getOrdem.get()
    c.execute("DELETE FROM tabelinha WHERE ordem = ?", (n_ordem,))
    conectar.commit()
    btPrimeiro_click()

def btSalvar_click() :
    lbAgora = Label(janela, text="Agora vc quer Salvar      ")
    lbAgora.place(x=200, y=370)

def btPrimeiro_click():
    lbAgora = Label(janela, text= "primeiro registro        ")
    lbAgora.place(x=200, y=370)
    getOrdem.delete(0, END)
    getOrdem.insert(0, "1")
    #n_ordem = 1
    btMostrar_click()

def btAnterior_click():
    lbAgora = Label(janela, text= "Registro anterior        ")
    lbAgora.place(x=200, y=370)
    n_ordem = int(getOrdem.get())
    ordem_menor = n_ordem - 1
    getOrdem.delete(0, END)
    getOrdem.insert(0, ordem_menor)
    #n_ordem = n_ordem - 1
    btMostrar_click()

def btProximo_click():
    n_ordem = int(getOrdem.get())
    ordem_maior = n_ordem + 1
    getOrdem.delete(0, END)
    getOrdem.insert(0, ordem_maior)
    #n_ordem= n_ordem + 1
    btMostrar_click()

def btUltimo_click():
    sqltotal= 'SELECT * FROM tabelinha'
    c.execute(sqltotal)
    n_total= c.fetchall() # todas as linhas da tabela
    getOrdem.delete(0, END)
    getOrdem.insert(0, len(n_total)) # len(n_total) resulta no número de registros
    btMostrar_click()
'''
def TotalRegistros():
    sqltotal= 'SELECT * FROM tabelinha'
    c.execute(sqltotal)
    n_total= c.fetchall()
    print('total de registros é ',n_total)
'''

def btMostrar_click():
    n_ordem = int(getOrdem.get())
    getNome.delete(0, END)
    getSobrenome.delete(0, END)
    getTelefone.delete(0, END)

    mostrar_nome = 'SELECT nome FROM tabelinha WHERE ordem = ?'
    for linha in c.execute(mostrar_nome, (n_ordem,)) :
        getNome.insert(0, linha)

    mostrar_sobrenome = 'SELECT sobrenome FROM tabelinha WHERE ordem = ?'
    for linha_sobrenome in c.execute(mostrar_sobrenome, (n_ordem,)):
        getSobrenome.insert(0, linha_sobrenome)

    mostrar_telefone = 'SELECT telefone FROM tabelinha WHERE ordem = ?'
    for linha_telefone in c.execute(mostrar_telefone, (n_ordem,)):
        getTelefone.insert(0, linha_telefone)

def btLimpar_click():
    getOrdem.delete(0, END)
    getNome.delete(0, END)
    getSobrenome.delete(0, END)
    getTelefone.delete(0, END)

def btSortear_click():
    sqltotal= 'SELECT * FROM tabelinha'
    c.execute(sqltotal)
    n_total= c.fetchall()
    #getOrdem.delete(0, END)
    #getOrdem.insert(0, len(n_total))
    quantos = len(n_total)

    n_rand= randint(1,quantos)
    n_ordem = n_rand
    #lbTestando["text"]= n_rand
    getOrdem.delete(0, END)
    getOrdem.insert(0, n_ordem)
    btMostrar_click()

btInserir = Button(janela, width=12, text= "Inserir", command= btInserir_click)
btInserir.place(x=100,y=300)

btAlterar = Button(janela, width=12, text= "Alterar", command= btAlterar_click)
btAlterar.place(x=200,y=300)

btExcluir = Button(janela, width=12, text= "Excluir", command= btExcluir_click)
btExcluir.place(x=300,y=300)

btPrimeiro = Button(janela, width=5, text= "<<", command= btPrimeiro_click)
btPrimeiro.place(x=100,y=330)

btAnterior = Button(janela, width=5, text= "<", command= btAnterior_click)
btAnterior.place(x=150,y=330)

btProximo = Button(janela, width=5, text= ">", command= btProximo_click)
btProximo.place(x=200,y=330)

btUltimo = Button(janela, width=5, text= ">>", command= btUltimo_click)
btUltimo.place(x=250,y=330)

btSalvar = Button(janela, width=12, text= "Salvar", command= btSalvar_click)
btSalvar.place(x=400,y=300)

btMostrar = Button(janela, width=12, text= "Mostrar", command= btMostrar_click)
btMostrar.place(x=200, y=150)

btLimpar = Button(janela, width=12, text= "Limpar", command= btLimpar_click)
btLimpar.place(x=300, y=150)

btSortear = Button(janela, width=12, text= "Sortear", command= btSortear_click)
btSortear.place(x=450, y=150)

lbOrdem = Label(janela, text="Ordem: ")
lbOrdem.place(x=50, y=50)
getOrdem= Entry(janela, width=5)
getOrdem.place(x=130, y=50)

lbNome = Label(janela, text="Nome: ")
lbNome.place(x=50, y=70)
getNome= Entry(janela, width=50)
getNome.place(x=130, y=70)
lb2Nome = Label(janela, text="Nome----- ")
lb2Nome.place(x=450, y=70)

lbSobrenome = Label(janela, text="Sobrenome: ")
lbSobrenome.place(x=50, y=90)
getSobrenome= Entry(janela, width=50)
getSobrenome.place(x=130, y=90)
lb2Sobrenome = Label(janela, text="Sobrenome----- ")
lb2Sobrenome.place(x=450, y=90)

lbTelefone = Label(janela, text="Telefone: ")
lbTelefone.place(x=50, y=110)
getTelefone= Entry(janela, width=50)
getTelefone.place(x=130, y=110)
lb2Telefone = Label(janela, text="Telefone----- ")
lb2Telefone.place(x=450, y=110)

janela.geometry("600x400+500+500")

janela.mainloop()