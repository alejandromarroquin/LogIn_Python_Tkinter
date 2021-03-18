# title: Login and Users System
# class: UserTrait
# description: Establish communication with the database
# author: Alejandro Marroquín Cruz
# contact: alejandroc.marroquin@gmail.com

from Database.Connect import Connect
from tkinter import messagebox
import hashlib

class UserTrait:

    @staticmethod
    def login(user):
        try:
            connection=Connect()
            db=connection.config_connect()
            fcursor=db.cursor()
            result=fcursor.execute("SELECT name,type FROM User WHERE email=%(email)s AND password=%(password)s",{'email':user.email,'password':hashlib.sha256(str(user.password).encode('utf-8')).hexdigest()})
            data=fcursor.fetchall()
            db.close()
            return result,data
        except:
            messagebox.showerror(title="Error",message="Error al establecer conexión con la base de datos")
            return 0,None

    @staticmethod
    def resgisterUser(user):
        try:
            connection=Connect()
            db=connection.config_connect()
            fcursor=db.cursor()
            fcursor.execute("INSERT INTO User (name, email, password, type) VALUES (%(name)s, %(email)s, %(password)s, %(type)s)",{'name':user.name,'email':user.email,'password':hashlib.sha256(str(user.password).encode('utf-8')).hexdigest(),'type':user.type})
            db.commit()
            return True
        except:
            messagebox.showerror(title="Error",message="Error al establecer conexión con la base de datos")
            return False