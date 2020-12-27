from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {"student": name}


api.add_resource(
    Student, "/student/<string:name>"
)  # http://127.0.0.1:5000/student/<name>
