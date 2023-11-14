from ...app import app
from ....session.verfDatas import SearchToDatabase 
from flask import (
    make_response, jsonify, request
)
from flask import session
from flask_jwt import jwt
from datetime import datetime,timedelta
from .....domain.validators.email import (
    validatorEmail
)
from .....domain.validators.password import (
    validatorPassword
)






@app.route('/user/login/<password>/<email>', methods=['get'])
def login(password, email):

    RESPONSE_EMAIL = validatorEmail.validate(email=email)
    RESPONSE_PASSWORD = validatorPassword.validate(password=password)

    if RESPONSE_PASSWORD["status"] and RESPONSE_EMAIL["status"]:
        response_login = SearchToDatabase(password, email)

        if response_login["status"]:
            time_now = datetime.utcnow()
            time_after = timedelta(weeks=4)
            secret_key = app.config['SECRET_KEY']

            payload = {
                "id": response_login["datas"]["id"],
                "exp": time_now + time_after
            }

            token = jwt.encode(payload, secret_key)
            session["token-login"] = token

            return make_response(jsonify({
                "response": {
                    "msg":"user authenticated",
                    "status": response_login,
                    "token":token
                }
            }))
    
    return make_response(jsonify({
        "response": {
            "msg":"user dont authenticated",
            "status":False
        }
    }))
