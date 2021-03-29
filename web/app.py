from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class Users(Resource):

    def get(self):

        with open('users.json', 'r', encoding='utf8') as J:

            return json.load(J)

class Permissions(Resource):

    def get(self):

        with open('permissions.json', 'r', encoding='utf8') as J:

            return json.load(J)

class Roles(Resource):

    def get(self):

        with open('roles.json', 'r', encoding='utf8') as J:

            return json.load(J)

class Services(Resource):

    def get(self):

        with open('services.json', 'r', encoding='utf8') as J:

            return json.load(J)

api.add_resource(Users, "/users")
api.add_resource(Permissions, "/permissions")
api.add_resource(Roles, "/roles")
api.add_resource(Services, "/services")


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)