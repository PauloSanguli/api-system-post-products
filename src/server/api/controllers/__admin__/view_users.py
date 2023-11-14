from flask import jsonify, make_response
from ...app import app
from .....utils.models._adminaccount import handlerAccountAdmin as Ihandler
from ...credentials.credentials_admin import IAdmin




@app.route('/admin/view_users/<password_admin>/', methods=["get"])
def view_users(password_admin): 
    
    adminCheck = IAdmin()
    response_adminCheck = adminCheck.isAdmin(password_admin)

    if response_adminCheck["status"]:
        db = Ihandler()
        response_select = db.select_users()
    else:
        return make_response(jsonify({
            "msg":"password admin wrong",
            "status":False
        }))

    return make_response(jsonify({
        "response":response_select
    }))
