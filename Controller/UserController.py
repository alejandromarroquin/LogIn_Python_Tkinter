# title: Login and Users System
# class: LoginController
# description: build the methods for the User CRUD 
# author: Alejandro Marroquín Cruz
# contact: alejandroc.marroquin@gmail.com

from Model.User import User
from Traits.UserTrait import UserTrait

class UserController:

    def __init__(self):
        pass

    def store(self,**kwargs):
        user=User()
        user.name=kwargs["name"]
        user.email=kwargs["email"]
        user.password=kwargs["password"]
        user.type=self.typeUser(kwargs["type"])
        return UserTrait.resgisterUser(user)

    @staticmethod
    def typeUser(typeuser):
        switcher = {
            "Administrador": "0",
            "Usuario A": "1",
            "Usuario B": "2",
            "Usuario C": "3"
        }
        return switcher.get(typeuser)

    @staticmethod
    def show(**kwargs):
        pass

    @staticmethod
    def edit(**kwargs):
        pass

    @staticmethod
    def update(**kwargs):
        pass

    @staticmethod
    def destroy(**kwargs):
        pass