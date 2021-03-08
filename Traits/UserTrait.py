from Database.Connect import Connect
import hashlib

class UserTrait:

    @staticmethod
    def login(user):
        connection=Connect()
        db=connection.config_connect()
        fcursor=db.cursor()
        result=fcursor.execute("SELECT name,type FROM User WHERE email='"+user.email+"' AND password='"+hashlib.sha256(str(user.password).encode('utf-8')).hexdigest()+"'")
        data=fcursor.fetchall()
        db.close()
        return result,data

    @staticmethod
    def resgisterUser(user):
        print(user.email)
        print(hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest())