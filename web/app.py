from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class Users(Resource):

    def get(self):

        with open('users.json', 'r', encoding='utf8') as J:

            return json.load(J)

    def post(self):

        pass

class User(Resource):

    def get(self, id):

        with open('users.json', 'r', encoding='utf8') as J:

            data = json.load(J)

            tam = len(data)

            for i in range(0, tam + 1):

                try:

                    if (data[i]["id"] == id):

                        return data[i]

                except:

                    J = {
                        "status": 404,
                        "message": "User not found"
                    }

                    return jsonify(J)

class UserFilter(Resource):

    def get(self, id, *args):

        with open('users.json', 'r', encoding='utf8') as J:

            return json.load(J)

class Members(Resource):

    def get(self):

        with open('members.json', 'r', encoding='utf8') as J:

            return json.load(J)

    def post(self):

        pass

class Permissions(Resource):

    def get(self):

        with open('permissions.json', 'r', encoding='utf8') as J:

            return json.load(J)

    def post(self):

        pass

class Roles(Resource):

    def get(self):

        with open('roles.json', 'r', encoding='utf8') as J:

            return json.load(J)

    def post(self):

        pass

class Services(Resource):

    def get(self):

        with open('services.json', 'r', encoding='utf8') as J:

            return json.load(J)

    def post(self):

        pass

api.add_resource(Users, "/users")
api.add_resource(User, "/users/<int:id>")
api.add_resource(Members, "/members")
api.add_resource(Permissions, "/permissions")
api.add_resource(Roles, "/roles")
api.add_resource(Services, "/services")


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)