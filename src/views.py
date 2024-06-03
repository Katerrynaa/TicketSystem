from flask import jsonify, request, Blueprint
from src.managers import  CreateUser, LoginUser, AuthUser
from src.schema import user_schema, login_schema
from marshmallow import ValidationError



auth = Blueprint('auth', __name__)



@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    try:
        user_schema.load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    
    response = CreateUser.create(data)
    return jsonify(response)



@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    try:
        login_schema.load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    
    username = data.get("username")
    password = data.get("password")
    response = LoginUser.login(username, password)
    return response



@auth.route("/tickets", methods=["POST"])
def authentication():
    data = request.get_json()
    try:
        login_schema.load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    
    username = data.get("username")
    password = data.get("password")
    response = AuthUser.authentication(username, password)
    return response 

