from ...app import app
from flask import (
    make_response, jsonify
)
from ...credentials.credential_articles import jwt_required_agend
from .....utils.models.accountpost import handlerPosts as Ihandler

#user_id, post_id, title_article, content_text, content_img, date_posted, price, show_post, date_post, time_post
@app.route('/user/agend_post/<title_article>/<content_text>/<price>/<date_agend>')
@jwt_required_agend
def user_agend_post(userid: int, title_article: str, content_text: str, price: float, date_agend):
    db = Ihandler()
    response = db.createPostAgend(userid, title_article, content_text, price, date_agend)

    return make_response(jsonify({
        "response": response
    }))
