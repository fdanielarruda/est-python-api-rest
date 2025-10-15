from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from hmac import compare_digest

from blacklist import BLACKLIST
from models.user import UserModel

attributes = reqparse.RequestParser()
attributes.add_argument('login', type=str, required=True)
attributes.add_argument('password', type=str, required=True)


class User(Resource):
    @jwt_required()
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except Exception as e:
                return {
                    'message': 'An internal error occurred trying to delete user.',
                    'error': str(e)
                }, 500

            return {'message': 'User deleted'}

        return {'message': 'User not found.'}, 404


class UserRegister(Resource):
    @classmethod
    def post(cls):
        data = attributes.parse_args()

        if UserModel.find_by_login(data['login']):
            return {"message": "The login '{}' already exists.".format(data['login'])}

        user = UserModel(**data)
        user.save_user()

        return {"message": "User created successfully!"}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = attributes.parse_args()

        user = UserModel.find_by_login(data['login'])
        if user and compare_digest(user.password, data['password']):
            access_token = create_access_token(identity=str(user.user_id))
            return {'access_token': access_token}, 200

        return {'message': 'The username or password is incorrect'}, 401

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully!'}, 200

