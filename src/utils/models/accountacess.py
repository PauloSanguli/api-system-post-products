from . import connectMySQL
from .querys.querysblockacess import querysMySQL



class defineAcessAccounts():
    def __init__(self):
        _objConnect = connectMySQL()
        response = _objConnect.connect()
        
        if response["status"]:
            self.db = response["connection"]
            self.cursor  = self.db.cursor()
        else:
            print("dont connected to database")



    def block_acess(self, user_id: int) -> dict:
        try:
            _SQL = querysMySQL.update_by_id(user_id, False)

            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("the acess was blocked", True)

    
    
    def unlock_acess(self, user_id: str) -> dict:
        try:
            _SQL = querysMySQL.update_by_id(user_id, True)

            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()

            return self.__returnResponse("the acess was unlocked", True)



    def __returnResponse(self, msg: str, status: bool) -> dict:
        return {
            "msg":f"{msg}",
            "status": status
        }
