from flask import current_app, make_response
from flask_jwt import wraps
from flask_jwt import jwt
from ....utils.models._adminaccount import handlerAccountAdmin as Ihandler
from flask import (
    session, request, jsonify
)



def jwt_required_recover(funct):
    wraps(funct)
    def wrapper_recover(*args, **kwargs):
        token = None
        secret_key = current_app.config['SECRET_KEY']
        _algorithms=['RS256','HS256']
        if 'token-cod' in session:
            token = session['token-cod']
            session.pop("token-cod")
        else:
            return make_response(jsonify({
                "response": {
                    "msg": "cod dont exist",
                    "status": False
                }
            }))

        try:
            decoded = jwt.decode(token, secret_key, algorithms=['RS256','HS256'])
            _email = decoded['email']
            db  = Ihandler()
            response_select = db.selectIduser(_email)
            _user_id = response_select["datas"]
            _cod = decoded['cod']
        except Exception as error:
            return make_response(jsonify({
                "response": {
                    "msg": "invalid token",
                    "status": False
                }
            }), 401)
        else:
            return funct(user_id=_user_id,cod=_cod,*args, **kwargs)
    return wrapper_recover



def jwt_required_changePWD(funct):
    wraps(funct)
    def wrapper_changePWD(*args, **kwargs):
        token = None
        title_header = 'x-access-token'

        if title_header in request.headers:
            token = request.headers[title_header]

        if not token:
            return jsonify({
                "msg": "invalid token",
                "status":False
            }), 401

        if not 'token' in token:
            return jsonify({
                "msg": "invalid token",
                "status":False
            }), 401
        
        Itoken = token.replace("token ", "")
        try:
            decoded = jwt.decode(Itoken, current_app.config['SECRET_KEY'],algorithms=['RS256','HS256'])
            _id = decoded["id"]
        except Exception:
            return jsonify({
                "msg":"You not logged",
                "status":False
            }), 401
        else:
            return funct(userid=_id, *args, **kwargs)
    return wrapper_changePWD