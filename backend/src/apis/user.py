from flask import Blueprint, jsonify

user = Blueprint("users", __name__, url_prefix="/user")


@user.route("/login", methods=["POST"])
def user_login():
    return jsonify({"message": "Invalid credentials"}), 401


@user.route("/", methods=["GET"])
def test():
    return jsonify({"message": "Invalid credentials"}), 401