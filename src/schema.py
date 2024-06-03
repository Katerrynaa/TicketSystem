from marshmallow import Schema, fields, validate


class RegisterUser(Schema):
    username = fields.String(required=True, validate=validate.Length(min=1))
    password = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.String(required=True)
    is_active = fields.Boolean(required=True)
    role_id = fields.Integer(required=True, validate=validate.Range(min=1))
    group_id = fields.Integer(required=True, validate=validate.Range(min=1))


class LoginUserSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=1))
    password = fields.String(required=True, validate=validate.Length(min=1))


user_schema = RegisterUser()
login_schema = LoginUserSchema()

