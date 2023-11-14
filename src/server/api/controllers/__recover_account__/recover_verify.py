from ...app import app
from flask_jwt import jwt
from datetime import datetime,timedelta
from flask import (
    make_response, jsonify,session
)
from ...credentials.credentials_recover_account import jwt_required_recover




@app.route('/user/recover_account/verify_cod/<cod_user>')
@jwt_required_recover
def recover_verify(user_id, cod, cod_user):
    if int(cod) == int(cod_user):
        time_now = datetime.utcnow()
        time_after = timedelta(weeks=4)
        secret_key = app.config['SECRET_KEY']

        payload = {
            "id": user_id,
            "exp": time_now + time_after
        }

        token = jwt.encode(payload, secret_key)
        session["token-login"] = token

        return make_response(jsonify({
            "response": {
                "msg": "cod authenticated, now change password",
                "status": True,
                "token": token
            }
        }), 200)

    return make_response(jsonify({
        "response": {
            "msg": "cod not authenticated",
            "status": False
        }
    }))
    