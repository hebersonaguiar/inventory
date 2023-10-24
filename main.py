from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from flask_cors import CORS
from repositories import connection


app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "flash message"

@app.route('/test', methods=['GET'])
def test():
    try:
        cur = connection.get_connection()
        cur.execute("select * from test")
        data = cur.fetchall()

        return jsonify({'test': 'true'}), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close
        

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5000')
