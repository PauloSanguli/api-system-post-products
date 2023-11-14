from ...app import app
from flask import (
    make_response, jsonify
)
from ...credentials.credentials_recover_account import (
    jwt_required_changePWD
)
from .....domain.validators.password import validatorPassword as Ivalidator
from .....utils.models.recoveraccount import (
    handlerRecoverAccount as Ihandler
)



@app.route('/user/recover_account/change_password/<new>', methods=['get'])
@jwt_required_changePWD
def recover_verify(user_id, new):
    response_pwd = Ivalidator.validate(new)
    if response_pwd["status"]:
        db = Ihandler()
        response_change = db.updatePWDById(user_id, new)

        if response_change["status"]:
            return make_response(jsonify({
                "response": response_change
            }))
    
    return make_response(jsonify({
        "response": {
            "msg": "password not changed, send cod again",
            "status": False
        }
    }))
    