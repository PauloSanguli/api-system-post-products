from . import connectMySQL
from . import encryptPassword
from .querys.queryrecoveraccount import updatepwdById


class handlerRecoverAccount():
    def __init__(self):
        obj = connectMySQL()
        self.db = obj.connect()
        self.cursor = self.db.cursor()

    def updatePWDById(self, id: int, password: str) -> dict:
        try:
            hashed_pwd = encryptPassword(password)
            _SQL = updatepwdById(id, hashed_pwd)

            self.cursor.execute(_SQL["statement"], _SQL["args"])
            self.db.commit()
        except:
            return {
                "msg": "password dont updated",
                "status": False
            }
        else:
            return {
                "msg": "password updated",
                "status": True
            }
