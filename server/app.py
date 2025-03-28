from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from models import db, init_app as init_db
from routes import init_routes
import jwt

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=["http://localhost:3000"])  # Allow front-end origin

init_db(app)  # Initialize SQLAlchemy
init_routes(app)  # Initialize routes

# Middleware to verify Firebase token
def verify_token(token):
    from google.auth.transport import requests
    from google.oauth2 import id_token
    try:
        decoded = id_token.verify_firebase_token(token, requests.Request())
        return decoded
    except Exception as e:
        return None

@app.before_request
def auth_middleware():
    if request.path == "/save":
        auth_header = request.headers.get("Authorization")
        if not auth_header or "Bearer " not in auth_header:
            return jsonify({"error": "Unauthorized"}), 401
        token = auth_header.split("Bearer ")[1]
        user = verify_token(token)
        if not user:
            return jsonify({"error": "Invalid token"}), 401
        request.user = user

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], port=5000)