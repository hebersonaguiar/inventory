from repositories import connection
import app

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
