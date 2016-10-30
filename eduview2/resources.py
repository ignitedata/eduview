from flask import Response, jsonify
from flask_restful import Resource, abort
from pymongo import MongoClient
from bson.json_util import dumps
from . import models

client = MongoClient()
db = client.datasets

schools = models.Schools(db)
graduates = models.Graduates(db)

class SchoolsResource(Resource):
	def get(self, sid=None):
		return jsonify(self.get_data())

	def get_data(self):
		return "Ayylmao"

class SchoolResource(Resource):
	def get(self, sid=None):
		return jsonify(schools.for_id(sid))

class SchoolGraduatesResource(Resource):
	def get(self, sid=None):
		return jsonify(list(graduates.for_school(sid)))