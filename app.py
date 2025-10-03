from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)


app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'user': 'admin',
    'password': 'admin'
}

class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    birth_date = db.DateTimeField(required=True)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Users(Resource):
    def get(self):
        return UserModel.objects()
        #return {"message": "user 1"}


class User(Resource):
    def get(self):
        return {"message": "CPF"}

    def post(self):
        return {"message": "teste"}


api.add_resource(HelloWorld, '/')
api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
