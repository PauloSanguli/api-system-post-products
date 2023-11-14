import pymysql
import bcrypt


class connectMySQL():
    def __init__(self):
        super().__init__()
        ...
    
    def connect(self) -> dict:
        try:
            self.db = pymysql.connect(
                user='root',
                database='exercise',
                host='localhost'
            )
            self.cursor = self.db.cursor()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            return self.__returnResponse("connected to databse", True)

    def __returnResponse(self, msg: str, status: bool) -> dict:
        return {
            "msg":f"{msg}",
            "status":status,
            "connection":self.db
        }



def encryptPassword(password: str) -> str:
    try:
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    except Exception as error:
        return {
            "msg":"failed to encrypt password",
            "status": False
        }
    else:
        return {
            "msg":"password encypted",
            "datas":password_hash.decode('utf-8'),
            "status":True
        }
