from flask_jsonpify import jsonify
from repositories import connection
from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "flash message"

mysql = connection.get_connection(app)

@app.route('/test', methods=['GET'])
def test():
    try:
        print("Passei pelo try")
        cur = mysql.connection.cursor()
        cur.execute("select * from test")
        data = cur.fetchall()

        return jsonify({'test': 'true'}), 200
    except Exception as error:
        print("Passei pela ececao do try")
        return jsonify(error), 400
    finally:
        cur.close
        
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5000')
