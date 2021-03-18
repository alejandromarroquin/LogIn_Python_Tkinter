# title: Login and Users System
# class: LoginController
# description: Controls access to the system
# author: Alejandro Marroquín Cruz
# contact: alejandroc.marroquin@gmail.com

from Model.User import User

class LoginController:

    @staticmethod
    def function_login(**kwargs):
        user=User()
        user=user.login(kwargs["email"],kwargs["password"])
        if(user[0]):
            return True,user[1]
        else:
            return False,None