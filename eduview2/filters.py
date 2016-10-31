from flask import jsonify

def to_json(data, status=200):
	return jsonify({
		'count': len(data),
		'results': data
	})