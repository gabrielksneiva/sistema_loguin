#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Aug 08, 2021 06:21:15 PM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True




class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.programa = tk.Tk()
        self.programa.geometry("600x450+1857+287")
        self.programa.minsize(120, 1)
        self.programa.maxsize(2884, 1005)
        self.programa.resizable(1,  1)
        self.programa.title("Login")
        self.programa.configure(background="#202b73")

        self.frameCadastro = tk.Frame(self.programa)
        self.frameCadastro.place(relx=0.217, rely=0.178, relheight=0.7, relwidth=0.558)
        self.frameCadastro.configure(relief='groove')
        self.frameCadastro.configure(borderwidth="2")
        self.frameCadastro.configure(relief="groove")
        self.frameCadastro.configure(background="#3f11b9")

        self.Login = tk.Label(self.frameCadastro)
        self.Login.place(relx=0.358, rely=0.063, height=41, width=114)
        self.Login.configure(activeforeground="#ffffff")
        self.Login.configure(background="#3f11b9")
        self.Login.configure(disabledforeground="#a3a3a3")
        self.Login.configure(font="-family {Corbel} -size 20")
        self.Login.configure(foreground="#ffffff")
        self.Login.configure(text='''Login''')

        self.Entry1 = tk.Entry(self.frameCadastro)
        self.Entry1.place(relx=0.149, rely=0.413, height=20, relwidth=0.758)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.frameCadastro, show='*')
        self.Entry2.place(relx=0.149, rely=0.603, height=20, relwidth=0.758)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Login1Cadastro = tk.Label(self.frameCadastro)
        self.Login1Cadastro.place(relx=0.09, rely=0.286, height=41, width=114)
        self.Login1Cadastro.configure(activebackground="#f9f9f9")
        self.Login1Cadastro.configure(activeforeground="#ffffff")
        self.Login1Cadastro.configure(background="#3f11b9")
        self.Login1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Login1Cadastro.configure(font="-family {Corbel} -size 15")
        self.Login1Cadastro.configure(foreground="#ffffff")
        self.Login1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Login1Cadastro.configure(highlightcolor="black")
        self.Login1Cadastro.configure(text='''Usuário''')

        self.Login1Cadastro_1 = tk.Label(self.frameCadastro)
        self.Login1Cadastro_1.place(relx=0.06, rely=0.476, height=41, width=114)
        self.Login1Cadastro_1.configure(activebackground="#f9f9f9")
        self.Login1Cadastro_1.configure(activeforeground="#ffffff")
        self.Login1Cadastro_1.configure(background="#3f11b9")
        self.Login1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Login1Cadastro_1.configure(font="-family {Corbel} -size 15")
        self.Login1Cadastro_1.configure(foreground="#ffffff")
        self.Login1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Login1Cadastro_1.configure(highlightcolor="black")
        self.Login1Cadastro_1.configure(text='''Senha''')

        self.Button1Cadastro = tk.Button(self.frameCadastro, command=self.loginBackEnd)
        self.Button1Cadastro.place(relx=0.209, rely=0.73, height=34, width=97)
        self.Button1Cadastro.configure(activebackground="#ececec")
        self.Button1Cadastro.configure(activeforeground="#000000")
        self.Button1Cadastro.configure(background="#ffff00")
        self.Button1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro.configure(foreground="#000000")
        self.Button1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro.configure(highlightcolor="black")
        self.Button1Cadastro.configure(pady="0")
        self.Button1Cadastro.configure(text='''Logar''')

        self.Button1Cadastro_1 = tk.Button(self.frameCadastro, command=self.cadastro)
        self.Button1Cadastro_1.place(relx=0.537, rely=0.73, height=34, width=97)
        self.Button1Cadastro_1.configure(activebackground="#ececec")
        self.Button1Cadastro_1.configure(activeforeground="#000000")
        self.Button1Cadastro_1.configure(background="#ffff00")
        self.Button1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_1.configure(foreground="#000000")
        self.Button1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_1.configure(highlightcolor="black")
        self.Button1Cadastro_1.configure(pady="0")
        self.Button1Cadastro_1.configure(text='''Cadastrar''')
        self.programa.mainloop()

    def cadastro(self):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.programa = tk.Tk()
        self.programa.geometry("600x450+1857+287")
        self.programa.minsize(120, 1)
        self.programa.maxsize(2884, 1005)
        self.programa.resizable(1, 1)
        self.programa.title("Cadastro")
        self.programa.configure(background="#202b73")

        self.frameCadastro = tk.Frame(self.programa)
        self.frameCadastro.place(relx=0.217, rely=0.178, relheight=0.7, relwidth=0.558)
        self.frameCadastro.configure(relief='groove')
        self.frameCadastro.configure(borderwidth="2")
        self.frameCadastro.configure(relief="groove")
        self.frameCadastro.configure(background="#3f11b9")

        self.Login = tk.Label(self.frameCadastro)
        self.Login.place(relx=0.358, rely=0.063, height=41, width=114)
        self.Login.configure(activeforeground="#ffffff")
        self.Login.configure(background="#3f11b9")
        self.Login.configure(disabledforeground="#a3a3a3")
        self.Login.configure(font="-family {Corbel} -size 20")
        self.Login.configure(foreground="#ffffff")
        self.Login.configure(text='''Cadastro''')

        self.Entry1Cadastro = tk.Entry(self.frameCadastro)
        self.Entry1Cadastro.place(relx=0.149, rely=0.413, height=20, relwidth=0.758)
        self.Entry1Cadastro.configure(background="white")
        self.Entry1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry1Cadastro.configure(font="TkFixedFont")
        self.Entry1Cadastro.configure(foreground="#000000")
        self.Entry1Cadastro.configure(insertbackground="black")

        self.Entry2Cadastro = tk.Entry(self.frameCadastro, show='*')
        self.Entry2Cadastro.place(relx=0.149, rely=0.603, height=20, relwidth=0.758)
        self.Entry2Cadastro.configure(background="white")
        self.Entry2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry2Cadastro.configure(font="TkFixedFont")
        self.Entry2Cadastro.configure(foreground="#000000")
        self.Entry2Cadastro.configure(insertbackground="black")

        self.Login1Cadastro = tk.Label(self.frameCadastro)
        self.Login1Cadastro.place(relx=0.09, rely=0.286, height=41, width=114)
        self.Login1Cadastro.configure(activebackground="#f9f9f9")
        self.Login1Cadastro.configure(activeforeground="#ffffff")
        self.Login1Cadastro.configure(background="#3f11b9")
        self.Login1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Login1Cadastro.configure(font="-family {Corbel} -size 15")
        self.Login1Cadastro.configure(foreground="#ffffff")
        self.Login1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Login1Cadastro.configure(highlightcolor="black")
        self.Login1Cadastro.configure(text='''Usuário''')

        self.Login1Cadastro_1 = tk.Label(self.frameCadastro)
        self.Login1Cadastro_1.place(relx=0.06, rely=0.476, height=41, width=114)
        self.Login1Cadastro_1.configure(activebackground="#f9f9f9")
        self.Login1Cadastro_1.configure(activeforeground="#ffffff")
        self.Login1Cadastro_1.configure(background="#3f11b9")
        self.Login1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Login1Cadastro_1.configure(font="-family {Corbel} -size 15")
        self.Login1Cadastro_1.configure(foreground="#ffffff")
        self.Login1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Login1Cadastro_1.configure(highlightcolor="black")
        self.Login1Cadastro_1.configure(text='''Senha''')


        self.Button1Cadastro_1 = tk.Button(self.frameCadastro, command=self.cadastrarBackEnd)
        self.Button1Cadastro_1.place(relx=0.537, rely=0.73, height=34, width=97)
        self.Button1Cadastro_1.configure(activebackground="#ececec")
        self.Button1Cadastro_1.configure(activeforeground="#000000")
        self.Button1Cadastro_1.configure(background="#ffff00")
        self.Button1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_1.configure(foreground="#000000")
        self.Button1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_1.configure(highlightcolor="black")
        self.Button1Cadastro_1.configure(pady="0")
        self.Button1Cadastro_1.configure(text='''Cadastrar''')
        self.programa.mainloop()

    def cadastrarBackEnd(self):
        try:
            with open('usuarios.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry1Cadastro.get() + '\n')


            with open('senhas.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry2Cadastro.get() + '\n')
            self.programa.destroy()
        except:
            print("Houve um erro!")

    def loginBackEnd(self):
        with open('usuarios.txt', 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()



        with open('senhas.txt', 'r') as arquivoUsuario:
            senhas = arquivoUsuario.readlines()


        usuarios = list(map(lambda x: x.replace('\n', ''), usuarios))

        senhas = list(map(lambda x: x.replace('\n', ''), senhas))

        usuario = self.Entry1.get()
        senha  = self.Entry2.get()

        logado = False

        for i in range(len(usuarios)):
            if usuario == usuarios[i] and senha == senhas[i]:
                print("Usuário logado!")
                self.programa.destroy()
                logado = True

            if not logado:
                print("Usuario/Senha inválidos, tente novamente!")
                self.programa.destroy()


Toplevel1()





