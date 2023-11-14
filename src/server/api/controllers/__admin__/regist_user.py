from flask import jsonify, make_response
from ...app import app
from .....utils.models._adminaccount import handlerAccountAdmin as Ihandler
from ...credentials.credentials_admin import IAdmin
from .....domain.validators.email import (
    validatorEmail
)
from .....domain.validators.password import (
    validatorPassword
)



@app.route('/admin/regist_user/<password_admin>/<username>/<passworduser>/<emailuser>/', methods=["get"])
def register(password_admin, username, passworduser, emailuser): 
    
    adminCheck = IAdmin()
    response_adminCheck = adminCheck.isAdmin(password_admin)

    if response_adminCheck["status"]:
        RESPONSE_EMAIL = validatorEmail.validate(emailuser)
        RESPONSE_PASSWORD = validatorPassword.validate(passworduser)

        if RESPONSE_EMAIL["status"] and RESPONSE_PASSWORD["status"]:
            db = Ihandler()
            response_create = db.createAccount(
                username=username,
                password=passworduser,
                email=emailuser
            )
        else:
            return make_response(jsonify({
                "msg":"failed to regist user, data wrong",
                "status":False
            }))
    else:
        return make_response(jsonify({
            "msg":"password admin wrong",
            "status":False
        }))

    return make_response(jsonify({
        "response": response_create
    }))
