# title: Login and Users System
# class: HomeView
# description: Build the main view for the type of user that logged in
# author: Alejandro Marroquín Cruz
# contact: alejandroc.marroquin@gmail.com

import tkinter
from tkinter import messagebox
from tkinter import ttk
from Controller.UserController import UserController

class HomeView:

    def __init__(self):
        self.window=None
        self.sidebar=None
        self.mainarea=None


    def window_home(self):
        # window
        self.window = tkinter.Tk()
        self.window.title("Inicio")
        self.window.geometry("1000x550+170+100")
        self.window.minsize(width=1000, height=550)
        self.window.maxsize(width=1000, height=550)
        # sidebar
        self.sidebar = tkinter.Frame(self.window, width=200, bg='#1B2631', height=550, borderwidth=2)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        # main content area
        self.mainarea = tkinter.Frame(self.window, width=500, height=500)
        self.mainarea.pack(expand=True, fill='both', side='right')


class UserAdmin(HomeView):

    def window_userAdmin(self):
        self.window_home()
        label = tkinter.Label(self.sidebar,text="Home Usario Administrador",fg="white",bg="#1B2631",height="3")
        label.pack()

        option_registeruser = tkinter.Label(self.sidebar,text="Registrar Usuario",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option_registeruser.pack(fill=tkinter.BOTH)
        option_registeruser.bind('<Button-1>',self.frame_registerUser)

        option1 = tkinter.Label(self.sidebar,text="Opción 1",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option1.pack(fill=tkinter.BOTH)
        option1.bind('<Button-1>',self.actions_option1)

        option2 = tkinter.Label(self.sidebar,text="Opción 2",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option2.pack(fill=tkinter.BOTH)
        option2.bind('<Button-1>',self.actions_option2)

        option2 = tkinter.Label(self.sidebar,text="Cerrar sesión",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option2.pack(fill=tkinter.BOTH)
        option2.bind('<Button-1>',self.cerrar_sesion)

    def frame_registerUser(self,event):
        self.mainarea.destroy()
        self.mainarea = tkinter.Frame(self.window, width=500, height=500)
        self.mainarea.pack(expand=True, fill='both', side='right')
        label = tkinter.Label(self.mainarea,text="Registrar Usuario",height="3")
        label.pack()

        name = tkinter.Label(self.mainarea,text="Nombre:",height=3,borderwidth=1, relief="flat")
        name.place(x=150,y=80)
        entry_name = tkinter.StringVar()
        input_name = tkinter.Entry(self.mainarea,textvariable=entry_name)
        input_name.place(x=280,y=90,width=350,height=30)

        email = tkinter.Label(self.mainarea,text="Correo:",height=3,borderwidth=1, relief="flat")
        email.place(x=150,y=160)
        entry_email = tkinter.StringVar()
        input_email = tkinter.Entry(self.mainarea,textvariable=entry_email)
        input_email.place(x=280,y=170,width=350,height=30)

        password = tkinter.Label(self.mainarea,text="Contraseña:",height=3,borderwidth=1, relief="flat")
        password.place(x=150,y=240)
        entry_password = tkinter.StringVar()
        input_password = tkinter.Entry(self.mainarea,textvariable=entry_password,show="*")
        input_password.place(x=280,y=250,width=350,height=30)

        typeuser = tkinter.Label(self.mainarea,text="Tipo de Usuario:",height=3,borderwidth=1, relief="flat")
        typeuser.place(x=150,y=320)
        entry_typeuser = tkinter.StringVar()
        input_typeuser = ttk.Combobox(self.mainarea, textvariable=entry_typeuser, values=["Administrador", "Usuario A", "Usuario B", "Usuario C"])
        input_typeuser.place(x=280,y=330,width=350,height=30)

        button_registeruser = tkinter.Button(self.window,text="Registrar",bg="#C2C2C2",fg="#000000",width="20",command=lambda:self.registerUser(entry_name,entry_email,entry_password,entry_typeuser))
        button_registeruser.place(x=500,y=430)

    @staticmethod
    def registerUser(name,email,password,typeuser):
        usercontroll=UserController()
        if usercontroll.store(name=name.get(),email=email.get(),password=password.get(),type=typeuser.get()):
            messagebox.showinfo(title="Success",message="Registro correcto")


    def actions_option1(self,event):
        self.mainarea.destroy()
        self.mainarea = tkinter.Frame(self.window, width=500, height=500)
        self.mainarea.pack(expand=True, fill='both', side='right')
        label = tkinter.Label(self.mainarea,text="Vista de la opción 1",height="3")
        label.pack()

    def actions_option2(self,event):
        self.mainarea.destroy()
        self.mainarea = tkinter.Frame(self.window, width=500, height=500)
        self.mainarea.pack(expand=True, fill='both', side='right')
        label = tkinter.Label(self.mainarea,text="Vista de la opción 2",height="3")
        label.pack()
    
    def cerrar_sesion(self,event):
        self.window.destroy()


class UserA(HomeView):

    def window_userA(self):
        self.window_home()
        label = tkinter.Label(self.sidebar,text="Home Usuario Tipo A",fg="white",bg="#1B2631",height="3")
        label.pack()

        option1 = tkinter.Label(self.sidebar,text="Opción 1A",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option1.bind('<Button-1>',self.actions_option1)
        option1.pack(fill=tkinter.BOTH)

        option2 = tkinter.Label(self.sidebar,text="Opción 2A",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option2.pack(fill=tkinter.BOTH)
        option2.bind('<Button-1>',self.actions_option2)

        option3 = tkinter.Label(self.sidebar,text="Opción 3A",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option3.pack(fill=tkinter.BOTH)
        option3.bind('<Button-1>',self.actions_option3)

    @staticmethod
    def actions_option1(event):
        print('Aquí se realizan las acciones de la opción 1A')

    @staticmethod
    def actions_option2(event):
        print('Aquí se realizan las acciones de la opción 2A')

    @staticmethod
    def actions_option3(event):
        print('Aquí se realizan las acciones de la opción 3A')

class UserB(HomeView):

    def window_userB(self):
        self.window_home()
        label = tkinter.Label(self.sidebar,text="Home Usuario Tipo B",fg="white",bg="#1B2631",height="3")
        label.pack()

        option1 = tkinter.Label(self.sidebar,text="Opción 1B",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option1.bind('<Button-1>',self.actions_option1)
        option1.pack(fill=tkinter.BOTH)

        option2 = tkinter.Label(self.sidebar,text="Opción 2B",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option2.pack(fill=tkinter.BOTH)
        option2.bind('<Button-1>',self.actions_option2)

        option3 = tkinter.Label(self.sidebar,text="Opción 3B",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option3.pack(fill=tkinter.BOTH)
        option3.bind('<Button-1>',self.actions_option3)

    @staticmethod
    def actions_option1(event):
        print('Aquí se realizan las acciones de la opción 1B')

    @staticmethod
    def actions_option2(event):
        print('Aquí se realizan las acciones de la opción 2B')

    @staticmethod
    def actions_option3(event):
        print('Aquí se realizan las acciones de la opción 3B')
