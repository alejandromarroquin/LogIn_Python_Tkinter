import pymysql

class Connect:

    @staticmethod
    def config_connect():
        config=pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="login_system"
        )
        return config
            