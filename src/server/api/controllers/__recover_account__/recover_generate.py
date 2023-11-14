from ...app import app
from flask_jwt import jwt
from flask import (
    make_response, jsonify,session
)
from datetime import datetime
from datetime import timedelta
from .....utils.recover_account.generate_cod import generate_cod
from .....utils.recover_account.send_to_email import sendEmail
from .....utils.models._adminaccount import handlerAccountAdmin as Ihandler




@app.route('/user/recover_account/generate_cod/<email>')
def recover_generate_cod(email):
    db = Ihandler()
    email_exists = db.selectDatasByEmail(email)
    if email_exists:
        secret_key = app.config['SECRET_KEY']
        exp_token = datetime.utcnow() + timedelta(minutes=10)
        cod_recover = generate_cod()
        payload = {
            "cod": cod_recover,
            "email": email,
            "exp": exp_token
        }

        token = jwt.encode(payload, secret_key)
        ISendEmail = sendEmail("paulosanguli@gmail.com", "sanguli10")
        ISendEmail.configureMSG(payload["cod"], email)
        response = ISendEmail.SendMSG()
        session['token-cod'] = token
        if response["status"]:
            return make_response(jsonify({
               "response":  {
                    "msg": "the cod of 8 digits expire in 10 minutes",
                    "token": token,
                    "status": True
               }
            }))
        else:
            return make_response(jsonify({
                "response": {
                    "msg": "message dont sended to email",
                    "status": False
                }
            }))
    else:
        return make_response(jsonify({
            "response": {
                "msg": "the email dont exists",
                "status": False
            }
        }), 404)
