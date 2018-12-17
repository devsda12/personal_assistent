from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class cooleshit(Resource):
    def get(self):
        return "This is cool"

class idk(Resource):
    def get(self):
        lol = "IDK Anymore"
        return lol

class lol(Resource):
    def get(self):
        lol = "LOLLOS"
        return lol

api.add_resource(cooleshit, "/cooleshit")
api.add_resource(idk, "/idk")
api.add_resource(lol, "/lol")

app.run()