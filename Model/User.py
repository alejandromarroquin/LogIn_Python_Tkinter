# title: Login and Users System
# class: User
# description: User Class build an object with attributes and methods Getter and Setter 
# author: Alejandro Marroquín Cruz
# contact: alejandroc.marroquin@gmail.com

from Traits import UserTrait

class User:

    def __init__(self):
        self._name=""
        self._email=""
        self._password=""
        self._type=""

    #Getter name
    @property
    def name(self):
        return self._name

    #Setter name
    @name.setter
    def name(self, name):
        self._name=name

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