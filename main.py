from repositories import connection
# import app
from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "flash message"

@app.route('/test', methods=['GET'])
def test():
    try:
        print("Passei pelo try")
        cur = connection.get_connection()
        cursor = cur.connection.cursor()
        cursor.execute("select * from test")
        data = cursor.fetchall()

        return jsonify({'test': 'true'}), 200
    except Exception as error:
        print("Passei pela ececao do try")
        return jsonify(error), 400
    finally:
        cursor.close
        
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5000')
