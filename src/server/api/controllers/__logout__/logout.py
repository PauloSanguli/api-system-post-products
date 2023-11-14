from flask import (
    request, session, make_response, jsonify
)
from ....api.app import app
from ...credentials.credentials_logout import jwt_required_logout


@app.route('/user/logout/', methods=['get'])
@jwt_required_logout
def user_logout(arg=""):
    if request.method == "GET":
        if 'token-login' in session:
            session.clear()
        
            return make_response(jsonify({
                "msg":"session destroyed",
                "status":True
            }))
        
        return make_response(jsonify({
            "msg": "you are not logged",
            "status": False
        }))
