from . import connectMySQL
from ..models.querys.queryaccountpost import querysMySQL




class handlerPosts():
    def __init__(self):
        _objConnect = connectMySQL()
        response = _objConnect.connect()
        
        if response["status"]:
            self.db = response["connection"]
            self.cursor  = self.db.cursor()
        else:
            print("don't connected to database")



    def createPost(self, user_id: int, title_article: str, content_text: str, price: float) -> dict :
        try:
            _SQL = querysMySQL.insert(user_id,title_article, content_text, price)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("post created", True)


    
    def createPostAgend(self, user_id: int, title_article: str, content_text: str, price: float, date_agend) -> dict :
        try:
            _SQL = querysMySQL.insertPostAgend(user_id,title_article, content_text, price, date_agend)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("post created", True)



    def selectPosts(self,user_id: int) -> dict:
        try:
            _SQL = querysMySQL.select_all(user_id)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
            datas = self.cursor.fetchall()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            response = self.__returnResponse("the datas was selected", True)
            response["datas"] = datas
            return response.copy()



    def deletePost(self,user_id: int, post_id: int) -> dict:
        try:
            _SQL = querysMySQL.delete(user_id, post_id)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("the post was deleted", True)



    def showPost(self, user_id: int, post_id: int) -> dict:
        try:
            _SQL = querysMySQL.update(user_id, post_id, True)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("the post is show", True)


        
    def hiddenPost(self, user_id: int, post_id: int) -> dict:
        try:
            _SQL = querysMySQL.update(user_id, post_id, False)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("the post is hidde", True)    



    def __returnResponse(self, msg: str, status: bool) -> dict:
        return {
            "msg":f"{msg}",
            "status": status
        }