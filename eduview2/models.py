class Schools:
	def __init__(self, db):
		self.schools = db.schools

	def for_id(self, sid):
		return self.schools.find_one({'id': sid}, {'_id': False})

class Graduates:
	def __init__(self, db):
		self.graduates = db.graduates

	def for_school(self, sid):
		return self.graduates.find({'school_data.id': sid}, {'_id': False})