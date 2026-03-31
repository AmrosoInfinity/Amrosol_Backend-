from flask import Blueprint, jsonify
from controllers.token_controller import get_token

token_bp = Blueprint("token", __name__)

@token_bp.route("/<service>/<userId>/<hashToken>")
def token(service, userId, hashToken):
    token_data = get_token(service, userId, hashToken)
    if token_data:
        return jsonify(token_data)
    return jsonify({"error": "Token expired or not found"}), 404
