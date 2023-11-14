from flask_jwt import jwt
from flask import current_app as app
from flask_jwt import wraps
from flask_jwt import request
from flask import jsonify





def jwt_required_name(funct):
    wraps(funct)
    def wrapper_name(*args, **kwargs):
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
        except Exception:
            return jsonify({
                "msg":"You not logged",
                "status":False
            }), 401
        else:
            return funct(userid=_id, *args, **kwargs)

    return wrapper_name



def jwt_required_date(funct):
    wraps(funct)
    def wrapper_date(*args, **kwargs):
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
        except Exception:
            return jsonify({
                "msg":"You not logged",
                "status":False
            }), 401
        else:
            return funct(userid=_id, *args, **kwargs)

    return wrapper_date


    
def jwt_required_email(funct):
    wraps(funct)
    def wrapper_email(*args, **kwargs):
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
        except Exception:
            return jsonify({
                "msg":"You not logged",
                "status":False
            }), 401
        else:
            return funct(userid=_id, *args, **kwargs)

    return wrapper_email



def jwt_required_phone(funct):
    wraps(funct)
    def wrapper_phone(*args, **kwargs):
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
        except Exception:
            return jsonify({
                "msg":"You not logged",
                "status":False
            }), 401
        else:
            return funct(userid=_id, *args, **kwargs)

    return wrapper_phone



def jwt_required_password(funct):
    wraps(funct)
    def wrapper_password(*args, **kwargs):
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
        except Exception:
            return jsonify({
                "msg":"You not logged",
                "status":False
            }), 401
        else:
            return funct(userid=_id, *args, **kwargs)

    return wrapper_password



def jwt_required_img(funct):
    wraps(funct)
    def wrapper_img(*args, **kwargs):
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
        except Exception:
            return jsonify({
                "msg":"You not logged",
                "status":False
            }), 401
        else:
            return funct(userid=_id, *args, **kwargs)

    return wrapper_img