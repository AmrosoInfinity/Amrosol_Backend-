from flask import Flask
from routes.token_routes import token_bp
from middleware.request_logger import request_logger

app = Flask(__name__)
app.before_request(request_logger)
app.register_blueprint(token_bp, url_prefix="/token")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
