from ..models import connectMySQL
from ..models import encryptPassword as encrypt
from ..models.querys.querysaccount import querysMySQL
from ..schema.viewUsersSchema import format_response
from ..schema.recoverSchema import format_response as format_id




class handlerAccountAdmin():
    def __init__(self):
        _objConnect = connectMySQL()
        response = _objConnect.connect()
        
        if response["status"]:
            self.db = response["connection"]
            self.cursor  = self.db.cursor()
        else:
            print("dont connected to database")

    

    def createAccount(self, username: str, password: str, email: str) -> dict:
        try:
            response = encrypt(password)
            _SQL = querysMySQL.insert(username, response["datas"], email)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
            self.db.commit()
            self.createAccountInfo(username, response["datas"], email)
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            return self.__returnResponse("the user was created", True)

    

    def select_users(self) -> dict:
        try:
            _SQL = querysMySQL.select_all()
            self.cursor.execute(_SQL["statement"])
            datas = self.cursor.fetchall()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()

            response = self.__returnResponse("datas selected", True)
            response["datas"] = format_response(datas)

            return response.copy()

    
    def selectIduser(self, email: str) -> dict:
        try:
            _SQL = querysMySQL.selectIdByEmail_(email)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
            datas = self.cursor.fetchall()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            response = self.__returnResponse("datas selected", True)
            response["datas"] = format_id(datas)

            return response.copy()


    def selectDatasByEmail(self, email: str) -> dict:
        try:
            _SQL = querysMySQL.selectAllByEmail(email)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
            datas = self.cursor.fetchall()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()

            response = self.__returnResponse("datas selected", True)
            response["datas"] = format_response(datas)

            return response.copy()


    def createAccountInfo(self, username: str, password: str, email: str) -> dict:
        try:
            _SQL = querysMySQL.selectIdByEmail(email, username)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
            id = self.cursor.fetchone()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            _SQL = querysMySQL.insertInfo(id, username, password, email)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
            self.db.commit()
            
            return self.__returnResponse("account created", True)


    def fetchUserLogged(self, id: int) -> dict:
        try:
            _SQL = querysMySQL.selectById(id)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
            datas = self.cursor.fetchone()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            response = self.__returnResponse("user authenticated",True)
            response["datas"] = datas

            return response.copy()
            

    def __returnResponse(self, msg: str, status: bool) -> dict:
        return {
            "msg":f"{msg}",
            "status": status
        }
