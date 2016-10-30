from flask.json import JSONEncoder
from bson.objectid import ObjectId

class MongoJSONEncoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, ObjectId):
			return str(obj)
		else:
			return obj