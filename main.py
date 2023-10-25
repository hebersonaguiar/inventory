from flask_jsonpify import jsonify
from repositories import connection
import app


mysql = connection.get_connection()

@app.app.route('/test', methods=['GET'])
def test():
    try:
        print("Passei pelo try")
        cur = mysql.connection.cursor()
        # cursor = cur.connection.cursor()
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
