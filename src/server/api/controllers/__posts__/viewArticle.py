from ...app import app
from .....utils.models.accountpost import (
    handlerPosts as Ihandler
)
from flask import (
    make_response, jsonify
)
from ...credentials.credential_articles import jwt_required_view
from .....utils._agend.verify_date_post import selectDates



@app.route('/user/post/view_posts/', methods=['get'])
@jwt_required_view
def user_view_post(userid):
    selectDates()
    db = Ihandler()
    response = db.selectPosts(
        user_id=userid
    )

    if response["status"]:
        return make_response(jsonify({
            "response": response
        }))
    else:
        return make_response(jsonify({
            "response":{
                "msg": "post dont selected",
                "status":False
            }
        }))
