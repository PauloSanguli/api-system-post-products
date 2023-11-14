from ...app import app
from .....utils.models.accountpost import (
    handlerPosts as Ihandler
)
from flask import (
    make_response, jsonify
)
from ...credentials.credential_articles import jwt_required_show





@app.route('/user/show_post/<int:postid>/', methods=['get'])
@jwt_required_show
def user_show_post(userid, postid):
    db = Ihandler()
    response = db.showPost(
        user_id=userid,
        post_id=postid
    )

    if response["status"]:
        return make_response(jsonify({
            "response":response
        }))
    else:
        return make_response(jsonify({
            "response":{
                "msg":"post dont showwed",
                "status":False
            }
        }))