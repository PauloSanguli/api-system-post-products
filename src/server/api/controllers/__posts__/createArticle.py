from ...app import app
from .....utils.models.accountpost import (
    handlerPosts as Ihandler
)
from flask import (
    make_response, jsonify
)
from ...credentials.credential_articles import jwt_required_create


@app.route('/user/create_post/<name>/<contenttext>/<pricearticle>', methods=['get'])
@jwt_required_create
def user_create_post(userid,name, contenttext, pricearticle):
    db = Ihandler()
    response = db.createPost(
        user_id=userid,
        content_text=contenttext,
        price=pricearticle,
        title_article=name
    )

    if response["status"]:
        return make_response(jsonify({
            "response":response
        }))
    else:
        return make_response(jsonify({
            "response":{
                "msg":"post dont created",
                "status":False
            }
        }))
