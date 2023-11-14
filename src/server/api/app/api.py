from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec


app = Flask(__name__)
app.config['SECRET_KEY'] = 'app-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/exercises'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

swagger_api = FlaskPydanticSpec("flask", title="Admin side")
swagger_api.register(app)