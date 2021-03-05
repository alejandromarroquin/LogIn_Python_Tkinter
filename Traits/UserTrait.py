from Database.Connect import Connect

class UserTrait:

    @staticmethod
    def login(user):
        connection=Connect()
        db=connection.config_connect()
        fcursor=db.cursor()
        result=fcursor.execute("SELECT name,type FROM User WHERE email='"+user.email+"' AND password='"+user.password+"'")
        data=fcursor.fetchall()
        db.close()
        return result,data

    @staticmethod
    def resgisterUser(user):
        print(user.email)