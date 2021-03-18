# title: Login and Users System
# class: LoginView
# description: Build the login view
# author: Alejandro Marroquín Cruz
# contact: alejandroc.marroquin@gmail.com

import tkinter
from Controller.LoginController import LoginController
from tkinter import messagebox
from View.HomeView import *

class LoginView:

    def __init__(self):
        self.entry_email = None
        self.entry_password = None
        self.window = None

    def window_login(self):
        self.window = tkinter.Tk()
        
        self.window.title("Login")

        self.window.geometry("600x400+400+150")
        self.window.minsize(width=600, height=400)
        self.window.maxsize(width=600, height=400)

        label = tkinter.Label(self.window,text="Inicio de Sesión",fg="white",bg="#1B2631",width="300",height="3")
        label.config(font=("Helvetica",12))
        label.pack()

        label_email = tkinter.Label(self.window,text="Correo:")
        label_email.place(x=150,y=95)
        self.entry_email = tkinter.StringVar()
        input_email = tkinter.Entry(self.window,textvariable=self.entry_email)
        input_email.place(x=150,y=120,width=300,height=30)

        label_password = tkinter.Label(self.window,text="Contraseña:")
        label_password.place(x=150,y=175)
        self.entry_password = tkinter.StringVar()
        input_password = tkinter.Entry(self.window,textvariable=self.entry_password,show="*")
        input_password.place(x=150,y=200,width=300,height=30)

        button_login = tkinter.Button(self.window,text="Iniciar sesión",bg="#C2C2C2",fg="#000000",width="20",command=lambda:self.login())
        button_login.place(x=220,y=270)

        self.window.mainloop()

    def login(self):
        access=LoginController.function_login(email=self.entry_email.get(),password=self.entry_password.get())
        if(access[0]):
            self.window.destroy()
            switch_semana = {
                '0': self.admin,
                '1': self.userA
            }
            switch_semana.get(access[1][0][1], 'Tipo de usuario incorrecto')()                
        else:
            messagebox.showinfo(title="Error",message="Acceso incorrecto")

    @staticmethod
    def admin():
        admin=UserAdmin()
        admin.window_userAdmin()

    @staticmethod
    def userA():
        user_a=UserA()
        user_a.window_userA()

