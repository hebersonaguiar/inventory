import threading
from app.app import application
from app.infrastructure.messaging.rabbitmq_consumer_runner import start_consumer

def run_flask_app():
    application.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':

    consumer_thread = threading.Thread(target=start_consumer, daemon=True)
    consumer_thread.start()
    
    run_flask_app()