import pymysql

class Connect:

    @staticmethod
    def config_connect():
        config=pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="pharmacy_sspc"
        )
        return config