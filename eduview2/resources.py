from flask import Response, request
from flask_restful import Resource, abort, reqparse
from pymongo import MongoClient
from bson.json_util import dumps
import time
from . import filters

client = MongoClient()
db = client.datasets

schools = db.schools
graduates = db.graduates

parser = reqparse.RequestParser()
parser.add_argument('offset', type=int, location='args')
parser.add_argument('ignore_limits', type=bool, location='args')

class SchoolsResource(Resource):
	def get(self):
		# Parse offset
		args = parser.parse_args()
		# Query MongoDB
		data = schools.find({}, {'_id': False})
		# Set a default limit for the API.
		# This is stupid. Fix it
		# TODO: Fix this hackery
		if not args['ignore_limits']:
			data = data.limit(5)

		if args['offset']:
			data = data.skip(args['offset'])

		# Typecast the list to prevent circular ref errors
		return filters.to_json(list(data))

class SchoolGPAResource(Resource):
	def get(self):
		return "5.0"

class MunicipalityGPAResource(Resource):
	def get(self):
		return "5.0"

class SchoolResource(Resource):
	def get(self, sid):
		data = [schools.find_one({'id': sid}, {'_id': False})]
		if data == []:
			abort(404)
		return filters.to_json(data)

class SchoolGraduatesResource(Resource):
	def get(self, sid):
		data = list(graduates.find({'school_data.id': sid}, {'_id': False}))
		return filters.to_json(data)

class MunicipalitiesResource(Resource):
	pass

class MunicipalityResource(Resource):
	pass

class AcademicRankingResource(Resource):
	pass
