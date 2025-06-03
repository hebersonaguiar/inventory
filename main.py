import threading
from app.app import application

def run_flask_app():
    application.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run_flask_app()