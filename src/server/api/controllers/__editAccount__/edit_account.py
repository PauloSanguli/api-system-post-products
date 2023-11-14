from flask import (
    make_response, jsonify
)
from .....domain.validators.name import (
    validatorName
)
from .....domain.validators.email import (
    validatorEmail
)
from .....domain.validators.password import (
    validatorPassword
)
from .....domain.validators.phone import (
    validatorPhoneNumber
)
from .....utils.models.editaccount import (
    handlerAccountUser as Ihandler
)
from ...credentials.credentials_edit_account import jwt_required_name
from ...credentials.credentials_edit_account import jwt_required_date
from ...credentials.credentials_edit_account import jwt_required_email
from ...credentials.credentials_edit_account import jwt_required_phone
from ...credentials.credentials_edit_account import jwt_required_img
from ...credentials.credentials_edit_account import jwt_required_password
from ...app import app





@app.route('/user/edit_name/<value>', methods=['get'])
@jwt_required_name
def edit_name(userid, value):
    response_name = validatorName.validate(value)
    if response_name["status"]:
        db = Ihandler()
        response_edit = db.editUsername(userid,value)
    else:
        response_edit = response_name.copy()

    return make_response(jsonify({
        "response": response_edit
    }))



@app.route('/user/edit_dateborn/<value>', methods=['get'])
@jwt_required_date
def edit_dateborn(userid, value):
    db = Ihandler()
    response_edit = db.editDateBorn(userid,value)

    return make_response(jsonify({
        "response": response_edit
    }))



@app.route('/user/edit_phonenumber/<value>', methods=['get'])
@jwt_required_phone
def edit_phonenumber(userid, value):
    db = Ihandler()
    response_validate = validatorPhoneNumber.validate(value)
    if response_validate["status"]:
        _phone = f'+244{value}'
        response_edit = db.editPhoneNumber(userid,_phone)
    else:
        response_edit = response_validate.copy()

    return make_response(jsonify({
        "response":response_edit
    }))



@app.route('/user/edit_img/<value>', methods=['get'])
@jwt_required_img
def edit_img(userid, value):
    db = Ihandler()
    response_edit = db.editImg(userid,value)

    return make_response(jsonify({
        "response":response_edit
    }))



@app.route('/user/edit_email/<value>', methods=['get'])
@jwt_required_email
def user_edit_email(userid, value):
    db = Ihandler()
    response = validatorEmail.validate(value)

    if response["status"]:
        response_edit = db.editEmail(userid,value)
    else:
        return make_response(jsonify({
            "response":response
        }))    

    return make_response(jsonify({
        "response":response_edit
    }))




@app.route('/user/edit_password/<old_password>/<new_password>', methods=['get'])
@jwt_required_password
def edit_password(userid, old_password, new_password):
    db = Ihandler()
    response = validatorPassword.validate(new_password)
    if response["status"]:
        response_edit = db.editPassword(userid, old_password, new_password)
    else:
        return make_response(jsonify({
            "msg":"invalid password",
            "status":False
        }))
    
    return make_response(jsonify({
        "response": response_edit
    }))
