from ...app import app
from .....utils.models.accountpost import (
    handlerPosts as Ihandler
)
from flask import (
    make_response, jsonify
)
from ...credentials.credential_articles import jwt_required_hidde




@app.route('/user/hidden_post/<int:postid>/', methods=['get'])
@jwt_required_hidde
def user_hidden_post(userid, postid):
    db = Ihandler()
    response = db.hiddenPost(
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
                "msg":"post dont hidden",
                "status":False
            }
        }))