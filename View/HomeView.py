import tkinter

class HomeView:

    def __init__(self):
        self.window=None
        self.sidebar=None


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
        mainarea = tkinter.Frame(self.window, width=500, height=500)
        mainarea.pack(expand=True, fill='both', side='right')


class UserAdmin(HomeView):

    def window_userAdmin(self):
        self.window_home()
        label = tkinter.Label(self.sidebar,text="Home Usario Administrador",fg="white",bg="#1B2631",height="3")
        label.pack()

        option_registeruser = tkinter.Label(self.sidebar,text="Registrar Usuario",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option_registeruser.bind('<Button-1>',self.registerUser)
        option_registeruser.pack(fill=tkinter.BOTH)

        option1 = tkinter.Label(self.sidebar,text="Opción 1",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option1.pack(fill=tkinter.BOTH)
        option1.bind('<Button-1>',self.actions_option1)

        option2 = tkinter.Label(self.sidebar,text="Opción 2",fg="white",bg="#1B2631",height=3,borderwidth=1, relief="flat",cursor="hand2")
        option2.pack(fill=tkinter.BOTH)
        option2.bind('<Button-1>',self.actions_option2)

    @staticmethod
    def registerUser(event):
        print('Aquí se registra un usuario')

    @staticmethod
    def actions_option1(event):
        print('Aquí se realizan las acciones de la opción 1')

    @staticmethod
    def actions_option2(event):
        print('Aquí se realizan las acciones de la opción 2')

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
