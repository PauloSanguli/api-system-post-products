from . import connectMySQL
from . import encryptPassword
from ..models.querys.queryeditaccount import querysMySQL
from ..models.querys.querysaccount import querysMySQL as Pwd
from ..schema.datasUserSchema import format_response
from ...server.session.verfDatas import check_hash




class handlerAccountUser():
    def __init__(self):
        _objConnect = connectMySQL()
        response = _objConnect.connect()
        
        if response["status"]:
            self.db = response["connection"]
            self.cursor  = self.db.cursor()
        else:
            print("don't connected to database")



    def editUsername(self,user_id: int, new: str) -> dict :
        try:
            _SQL = querysMySQL.update_name(user_id, new)
            self.cursor.execute(_SQL[0]["statement"], _SQL[0]["args"])
            self.cursor.execute(_SQL[1]["statement"], _SQL[1]["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("name updated", True)



    def editDateBorn(self,user_id: int, new: any) -> dict :
        try:
            _SQL = querysMySQL.update_date(user_id, new)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("date updated", True)



    def editPhoneNumber(self,user_id: int, new: str) -> dict :
        try:
            _SQL = querysMySQL.update_phone(user_id, new)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("phone updated", True)


    def editEmail(self,user_id: int, new: str) -> dict :
        try:
            _SQL = querysMySQL.update_email(user_id, new)
            self.cursor.execute(_SQL[0]["statement"], _SQL[0]["args"])
            self.cursor.execute(_SQL[1]["statement"], _SQL[1]["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("email updated", True)



    def editImg(self,user_id: int, new: any) -> dict :
        try:
            _SQL = querysMySQL.update_img(user_id, new)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("img updated", True)

    
    def editPassword(self,user_id: int, old: str, new: str) -> dict :
        try:
            _SQL = Pwd.selectPwdById(user_id)
            self.cursor.execute(_SQL["statement"], _SQL["args"])
            _password = self.cursor.fetchone()[0]

            if check_hash(_password, old):   
                hash_pwd = encryptPassword(new)
                _SQL = querysMySQL.update_password(user_id, hash_pwd["datas"])
                self.cursor.execute(_SQL["statement"], _SQL["args"])
            else:
                return self.__returnResponse("your old password is wrong", False)

        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            return self.__returnResponse("password updated", True)


    def viewDataUser(self, id: int) -> dict:
        try:
            _SQL = querysMySQL.viewData(id)

            self.cursor.execute(_SQL["statement"], _SQL["args"])
            data = self.cursor.fetchone()
        except Exception as error:
            return self.__returnResponse(error, False)
        else:
            self.db.commit()
            response = self.__returnResponse("datas selected", True)
            response["datas"] = format_response(data)

            return response.copy()

    
    def __returnResponse(self, msg: str, status: bool) -> dict:
        return {
            "msg":f"{msg}",
            "status": status
        }
