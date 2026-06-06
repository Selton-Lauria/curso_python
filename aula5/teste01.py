import tkinter as tk
from tkinter import messagebox
def cadastrar():
    nome=entry_nome.get()
    messagebox.showinfo("Cadastro", f"{nome} cadastrado com sucesso!")
janela = tk.Tk()
janela.title("Sistema de Notas")
janela.geometry("450x250")
janela.configure(bg="#F5F5F5")

# Título
tk.Label(janela, text="CENTRO UNIVERSITÁRIO -UNIESP").grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Nome
tk.Label(janela, text="Nome:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nome=tk.Entry(janela, width=40,font=("Arial", 11))
entry_nome.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Botão
tk.Button( janela, text="Cadastrar",command=cadastrar, bg="red", fg="white", width=20).grid(row=3, column=0, padx=10, pady=10, sticky="w")  

# Resultado
resultado=tk.Label(janela, text="Resultado:",bg="#F5F5F5")
resultado.grid(row=4, column=0, padx=10, pady=5, sticky="w")

janela.mainloop()