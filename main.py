from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd

# FUNÇÕES

# Função para adicionar um item à tabela
def add_item(table, df):
    print("oiducu")
    # Obtém o item a ser vendido
    item = input("Item a ser vendido: ")

    # Obtém a quantidade vendida
    quantidade = input("Quantidade vendida: ")

    # Obtém o preço do item
    preco = input("Preço do item: ")

    # Insere o item na tabela
    table.insert("", len(df), values=[item, quantidade, preco])

    # Adiciona o item à tabela Excel
    df.loc[len(df)] = [item, quantidade, preco]
    df.to_excel("itens_vendidos.xlsx")

#--------------------------------------------

# Carrega a tabela de itens vendidos do Excel
df = pd.read_excel("itens_vendidos.xlsx")

# Cria a janela principal
root = tk.Tk()
root.title("Interface de vendas")

# Cria a tabela de itens vendidos
table = tk.ttk.Treeview(root)
table["columns"] = ["Item", "Quantidade", "Preço"]
table.column("#0", width=100)
table.column("Item", anchor="w", width=200)
table.column("Quantidade", anchor="w", width=100)
table.column("Preço", anchor="w", width=100)

# Insere os dados da tabela  Excel na tabela
for i in range(df.shape[0]):
    table.insert("", i, values=[df.loc[i, "Item"], df.loc[i, "Quantidade"], df.loc[i, "Preço"]])

# Cria o menu de botões
frame = tk.Frame(root)
btn_add = tk.Button(frame, text="Adicionar item", command=lambda: add_item(table, df))
btn_exit = tk.Button(frame, text="Sair", command=root.quit)
frame.pack()
btn_add.pack(side="left")
btn_exit.pack(side="right")

# Inicia a janela principal
root.mainloop()