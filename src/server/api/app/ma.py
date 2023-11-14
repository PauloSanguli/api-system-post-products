from flask_marshmallow import Marshmallow
from .api import app

ma = Marshmallow(app)


class schemaUserdatas(ma.Schema):
    class Meta():
        fields = ('id','password','username','email')

send_one = schemaUserdatas()
send_more = schemaUserdatas(many=True)