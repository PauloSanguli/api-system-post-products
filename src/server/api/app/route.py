from .api import app
from flask import (
    make_response, jsonify
)


@app.route('/', methods=['get'])
def say_hello():
    return make_response(
        jsonify({
            "msg":"Api documentation on air!"
        })
    )
