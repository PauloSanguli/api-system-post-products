from flask_jwt import jwt
from flask import current_app as app
from flask_jwt import wraps
from flask_jwt import request
from flask import jsonify, request
from ....utils.models.editaccount import handlerAccountUser as Ihandler



    
def jwt_required(funct):
    wraps(funct)
    def wrapper(*args, **kwargs):
        print(request.args.get("test"))
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
            decoded = jwt.decode(Itoken, app.config['SECRET_KEY'],algorithms=['RS256','HS256'])
            _id = decoded["id"]
            db = Ihandler()
            _user = db.viewDataUser(_id)
        except Exception:
            return jsonify({
                "msg":"You not logged",
                "status":False
            }), 401
        else:
            return funct(user=_user, *args, **kwargs)

    return wrapper


