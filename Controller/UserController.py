
from Model.User import User
from Traits.UserTrait import UserTrait

class UserController:

    def __init__(self):
        pass

    @staticmethod
    def store(**kwargs):
        user=User()
        user.email=kwargs["email"]
        user.password=kwargs["password"]
        user.type=kwargs["type"]
        UserTrait.resgisterUser()

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