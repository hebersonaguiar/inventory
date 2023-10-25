from flask_jsonpify import jsonify
from repositories import connection
import app

app = app.application

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5000')
