from tkinter import messagebox
from packdata import *


class Backend:
    def __init__(self):
        self.Data = Data_Verificar()

    def Mostrar_senha(self, senha):
        if senha.cget('show') == '*':
            senha.config(show='')
        else:
            senha.config(show='*')

    def Cadastrar(self, cpf, nome, datanasc, email, senha, conf, c_m, c_f, c_a, c_e, frame_func, frame_cadas):
        if messagebox.askyesno('confirmar', 'salvar dados?'):
            self.Data.Cadastrar(cpf.get(), nome.get(), datanasc.get(), 'M', email.get(), senha.get(), 0)
            cpf.delete(0, 'end')
            nome.delete(0, 'end')
            datanasc.delete(0, 'end')
            email.delete(0, 'end')
            senha.delete(0, 'end')
            conf.delete(0, 'end')
            c_m.deselect()
            c_f.deselect()
            c_a.deselect()
            c_e.deselect()
            frame_func.pack()
            frame_cadas.forget()
        else:
            pass

    def Entrar_func(self, entry_func, entry_senha, frame_cadas, frame_func):
        if self.Data.Check_func(entry_func, entry_senha):
            frame_cadas.pack()
            frame_func.forget()
        else:
            messagebox.showerror('Acesso Negado', 'conta invalida, tente novamente')

    def Entrar_cli(self, entry_cpf, entry_senha, frame_conta, frame_entrar, frame_cli):
        if self.Data.Check_cli(entry_cpf, entry_senha):
            frame_conta.pack()
            frame_entrar.forget()
            frame_cli.forget()
        else:
            messagebox.showerror('Acesso Negado', 'conta desconhecida, tente novamente')

