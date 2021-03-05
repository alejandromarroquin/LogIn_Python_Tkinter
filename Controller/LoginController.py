
from Model.User import User
from Traits.UserTrait import UserTrait
from tkinter import messagebox

class LoginController:

    @staticmethod
    def function_login(**kwargs):
        user=User()
        user.email=kwargs["email"]
        user.password=kwargs["password"]
        login=UserTrait()
        if(login.login(user)[0]):
            messagebox.showinfo(title="Success",message="Acceso correcto")
        else:
            messagebox.showinfo(title="Error",message="Acceso incorrecto")