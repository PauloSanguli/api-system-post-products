from flask import jsonify, make_response, request
from ...app import app
from ...credentials.credentials_view_datas import jwt_required



@app.route('/user/view_datas_user/', methods=["get"])
@jwt_required
def view_datas_user(user): 
    if request.method == 'GET':
        return make_response(jsonify({
            "response": user
        }))
