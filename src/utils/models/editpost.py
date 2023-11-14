from . import connectMySQL
from ..models.querys.queryeditpost import querysMySQL




class editPost():
    def __init__(self):
        _objConnect = connectMySQL()
        response = _objConnect.connect()
        
        if response["status"]:
            self.db = response["connection"]
            self.cursor  = self.db.cursor()
        else:
            print("don't connected to database")



    def editTitle(self,user_id: int, post_id: int, new: str) -> dict :
        try:
            _SQL = querysMySQL.update_title(user_id, post_id, new)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("name updated", True)


    def editContent(self,user_id: int, post_id: int, new: str) -> dict :
        try:
            _SQL = querysMySQL.update_content(user_id, post_id, new)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("content updated", True)


    def editImg(self,user_id: int, post_id: int, new: any) -> dict :
        try:
            _SQL = querysMySQL.update_img(user_id, post_id, new)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("image updated", True)


    def editPrice(self,user_id: int, post_id: int, new: float) -> dict :
        try:
            _SQL = querysMySQL.update_price(user_id, post_id, new)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("price updated", True)



    def __returnResponse(self, msg: str, status: bool) -> dict:
        return {
            "msg":f"{msg}",
            "status": status
        }
