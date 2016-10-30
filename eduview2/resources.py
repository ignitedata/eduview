from flask_restful import Resource, abort
from . import models

class SchoolResource(Resource):
	def get(self, id=None):
		return self.get_school(10017)

	def get_school(self, sid):
		return models.get_by_id(sid)