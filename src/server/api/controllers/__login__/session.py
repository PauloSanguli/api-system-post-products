from ...app import app
from flask import (
    make_response, jsonify, request
)
from flask import session



@app.route('/user/verify_login/', methods=['get'])
def _session():
    if request.method == 'GET':
        if 'token-login' in session:
            return make_response(jsonify({
                "msg": "you are logged",
                "status": True,
                "token": session["token-login"]
            }))

        return make_response(jsonify({
            "msg": "you are not logged",
            "status": False
        }))