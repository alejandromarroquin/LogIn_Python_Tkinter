from Traits import UserTrait

class User:

    def __init__(self):
        self._email=""
        self._password=""
        self._type=""

    #Getter email
    @property
    def email(self):
        return self._email

    #Setter email
    @email.setter
    def email(self, email):
        self._email=email

    #Getter password
    @property
    def password(self):
        return self._password

    #Setter password
    @password.setter
    def password(self,password):
        self._password=password

    #Getter type
    @property
    def type(self):
        return self._type
    
    #Setter type
    @type.setter
    def type(self,type):
        self._type=type