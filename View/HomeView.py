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

class UserA(HomeView):

    def window_userA(self):
        self.window_home()
        label = tkinter.Label(self.sidebar,text="Home Usuario Tipo A",fg="white",bg="#1B2631",height="3")
        label.pack()

class UserB(HomeView):

    def window_userB(self):
        self.window_home()
        label = tkinter.Label(self.sidebar,text="Home Usuario Tipo B",fg="white",bg="#1B2631",height="3")
        label.pack()
