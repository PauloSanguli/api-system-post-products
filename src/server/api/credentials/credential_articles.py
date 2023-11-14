from flask_jwt import jwt
from flask import current_app as app
from flask_jwt import wraps
from flask_jwt import request
from flask import jsonify



    
def jwt_required_create(funct):
    wraps(funct)
    def wrapper_create(*args, **kwargs):
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

    return wrapper_create


def jwt_required_delete(funct):
    wraps(funct)
    def wrapper_delete(*args, **kwargs):
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

    return wrapper_delete


def jwt_required_show(funct):
    wraps(funct)
    def wrapper_show(*args, **kwargs):
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

    return wrapper_show


def jwt_required_hidde(funct):
    wraps(funct)
    def wrapper_hidde(*args, **kwargs):
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

    return wrapper_hidde


def jwt_required_view(funct):
    wraps(funct)
    def wrapper_view(*args, **kwargs):
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

    return wrapper_view


def jwt_required_update_title(funct):
    wraps(funct)
    def wrapper_update_title(*args, **kwargs):
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

    return wrapper_update_title


def jwt_required_update_content(funct):
    wraps(funct)
    def wrapper_update_content(*args, **kwargs):
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

    return wrapper_update_content


def jwt_required_update_img(funct):
    wraps(funct)
    def wrapper_update_img(*args, **kwargs):
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

    return wrapper_update_img


def jwt_required_update_price(funct):
    wraps(funct)
    def wrapper_update_price(*args, **kwargs):
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

    return wrapper_update_price



def jwt_required_agend(funct):
    wraps(funct)
    def wrapper_agend(*args, **kwargs):
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

    return wrapper_agend