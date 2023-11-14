from ..models import connectMySQL
from ..models.querys.queryaccountlogin import (
    querysMySQL
)



class handlerAccountLogin():
    def __init__(self):
        _objConnect = connectMySQL()
        response = _objConnect.connect()
        
        if response["status"]:
            self.db = response["connection"]
            self.cursor  = self.db.cursor()
        else:
            print("dont connected to database")



    def verify_datas(self, email: str) -> dict:
        try:
            _SQL = querysMySQL.select_by_Email(email)

            self.cursor.execute(_SQL["statement"], _SQL["args"])
            datas = self.cursor.fetchone()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            response = self.__returnResponse("datas checked", True)
            response["datas"] = datas

            return response.copy()



    def __returnResponse(self, msg: str, status: bool) -> dict:
        return {
            "msg":f"{msg}",
            "status": status
        }

