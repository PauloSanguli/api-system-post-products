import bcrypt
from ...utils.schema.loginSchema import format_response
from ...utils.models.accountlogin import (
    handlerAccountLogin as Ihandler
)


def SearchToDatabase(password: str, email: str) -> dict:
    db = Ihandler()
    response = db.verify_datas(email)

    if not response["status"]:
        return {
            "msg":"failed to login",
            "status":False
        }
    
    password_db = response["datas"][2]
    status_login = check_hash(password_db, password)
    response_datas = format_response(response["datas"])

    return {
        "status": status_login,
        "datas": response_datas
    }
   

def check_hash(hashedpassword: str, password: str) -> any:
    hashed_password = hashedpassword.encode('utf-8')

    response_bool = bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    return response_bool

