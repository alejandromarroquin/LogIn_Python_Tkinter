# title: Login and Users System
# class: User
# description: User Class build an object with attributes and methods Getter and Setter 
# author: Alejandro Marroquín Cruz
# contact: alejandroc.marroquin@gmail.com

from Database.Connect import Connect
from tkinter import messagebox
import hashlib

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

    @staticmethod
    def login(email,password):
        try:
            connection=Connect()
            db=connection.config_connect()
            fcursor=db.cursor()
            result=fcursor.execute("SELECT name,type FROM User WHERE email=%(email)s AND password=%(password)s",{'email':email,'password':hashlib.sha256(str(password).encode('utf-8')).hexdigest()})
            data=fcursor.fetchall()
            db.close()
            return result,data
        except:
            messagebox.showerror(title="Error",message="Error al establecer conexión con la base de datos")
            return 0,None

    def resgisterUser(self):
        try:
            connection=Connect()
            db=connection.config_connect()
            fcursor=db.cursor()
            fcursor.execute("INSERT INTO User (name, email, password, type) VALUES (%(name)s, %(email)s, %(password)s, %(type)s)",{'name':self.name,'email':self.email,'password':hashlib.sha256(str(self.password).encode('utf-8')).hexdigest(),'type':self.type})
            db.commit()
            return True
        except:
            messagebox.showerror(title="Error",message="Error al establecer conexión con la base de datos")
            return False