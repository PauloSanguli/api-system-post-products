from ...app import app
from .....utils.models.accountpost import (
    handlerPosts as Ihandler
)
from flask import (
    make_response, jsonify
)
from ...credentials.credential_articles import jwt_required_delete



@app.route('/user/delete_post/<int:postid>/', methods=['get','delete'])
@jwt_required_delete
def user_delete_post(userid, postid):
    db = Ihandler()
    response = db.deletePost(
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
                "msg":"post dont deleted",
                "status":False
            }
        }))
