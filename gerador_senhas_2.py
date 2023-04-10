import random
from tkinter import *

janela = Tk()
janela.geometry('400x400')
janela.title('Gerador de Senhas')

def gerar_senha():
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%¨&'
    senha = ''.join(random.choice(caracteres) for i in range (16))
    entrada_senha.configure(state='normal')
    entrada_senha.delete(0, END)
    entrada_senha.insert(0, senha)
    entrada_senha.configure(state='readonly')
botao = Button(janela, text="Gerar Senha", command=gerar_senha)
botao.grid(column=2, row=2, padx=10, pady=10)

label_senha = Label(janela, text="Senha gerada: ")
label_senha.grid(column=1, row=1, padx=10, pady=10)
entrada_senha = Entry(janela, width=40, state='readonly')
entrada_senha.grid(column=2, row=1, padx=10, pady=10)

janela.mainloop()
