from ...app import app
from ...credentials.credential_articles import jwt_required_update_title
from ...credentials.credential_articles import jwt_required_update_content
from ...credentials.credential_articles import jwt_required_update_img
from ...credentials.credential_articles import jwt_required_update_price
from .....utils.models.editpost import (
    editPost as Ihandler
)
from flask import (
    make_response, jsonify
)




@app.route('/user/post/edit_title/<int:postid>/<value>', methods=['get','patch'])
@jwt_required_update_title
def user_update_title(userid, postid, value):
    db = Ihandler()
    response = db.editTitle(
        user_id=userid,
        post_id=postid,
        new=value
    )

    if response["status"]:
        return make_response(jsonify({
            "response":response
        }))
    else:
        return make_response(jsonify({
            "response":{
                "msg":"post dont updated",
                "status":False
            }
        }))

@app.route('/user/post/edit_content/<int:postid>/<value>', methods=['get'])
@jwt_required_update_content
def user_update_content(userid, postid, value):
    db = Ihandler()
    response = db.editContent(
        user_id=userid,
        post_id=postid,
        new=value
    )

    if response["status"]:
        return make_response(jsonify({
            "response":response
        }))
    else:
        return make_response(jsonify({
            "response":{
                "msg":"post dont updated",
                "status":False
            }
        }))

@app.route('/user/post/edit_price/<int:postid>/<value>', methods=['get'])
@jwt_required_update_price
def user_update_price(userid, postid, value):
    db = Ihandler()
    response = db.editPrice(
        user_id=userid,
        post_id=postid,
        new=value
    )

    if response["status"]:
        return make_response(jsonify({
            "response":response
        }))
    else:
        return make_response(jsonify({
            "response":{
                "msg":"post dont updated",
                "status":False
            }
        }))

@app.route('/user/post/edit_img/<int:postid>/<value>', methods=['get'])
@jwt_required_update_img
def user_update_img(userid, postid, value):
    db = Ihandler()
    response = db.editImg(
        user_id=userid,
        post_id=postid,
        new=value
    )

    if response["status"]:
        return make_response(jsonify({
            "response":response
        }))
    else:
        return make_response(jsonify({
            "response":{
                "msg":"post dont updated",
                "status":False
            }
        }))