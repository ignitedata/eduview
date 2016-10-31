from flask import Flask
from flask_restful import Resource, Api
from eduview2 import resources
from eduview2 import encoders

app = Flask(__name__)
api = Api(app)

app.json_encoder = encoders.MongoJSONEncoder

api.add_resource(resources.SchoolsResource, '/schools/')
api.add_resource(resources.SchoolResource, '/schools/<int:sid>')
api.add_resource(resources.SchoolGraduatesResource, '/schools/<int:sid>/graduates')

if __name__ == '__main__':
	app.run(debug=True)