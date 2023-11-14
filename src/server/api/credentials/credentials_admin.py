import pymysql
from dataclasses import dataclass


@dataclass(frozen=False)
class IAdmin():
    def __init__(self):
        self.db = pymysql.connect(
                user='root',
                database='exercise',
                host='localhost'
            )
        self.cursor = self.db.cursor()
    
    def isAdmin(self, password: str) -> dict:
        self.cursor.execute("""SELECT * FROM `admin`""")
        datas = self.cursor.fetchone()

        if password == datas[2]:
            return self.__returnResponse("admin ckecked", True)
        else:
            return self.__returnResponse("You are not admin", False)

    def __returnResponse(self, msg: str, status: bool) -> dict:
        return {
            "msg":f"{msg}",
            "status":status
        }
