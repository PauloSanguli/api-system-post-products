from flask import jsonify, make_response
from ...app import app
from .....utils.models.accountacess import defineAcessAccounts as Ihandler
from ...credentials.credentials_admin import IAdmin




@app.route('/admin/acess/unlock/<password_admin>/<userid>/', methods=["get"])
def unlock_acess(password_admin, userid): 
    
    adminCheck = IAdmin()
    response_adminCheck = adminCheck.isAdmin(password_admin)

    if response_adminCheck["status"]:
        db = Ihandler()
        response_block = db.unlock_acess(userid)

    return make_response(jsonify({
        "response":response_block
    }))
