from Model.User import User
from Traits.UserTrait import UserTrait
class LoginController:

    @staticmethod
    def function_login(**kwargs):
        user=User()
        user.email=kwargs["email"]
        user.password=kwargs["password"]
        login=UserTrait()
        login=login.login(user)
        if(login[0]):
            return True,login[1]
        else:
            return False,None