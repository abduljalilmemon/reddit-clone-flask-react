from flask import Blueprint, jsonify

# from flask
user = Blueprint("users", __name__, url_prefix="/user")


@user.route("/login", methods=["POST"])
def login_user():
    return jsonify({"message": "Invalid credentials"}), 401


@user.route("/register", methods=["POST"])
def register_user():
    return jsonify({"message": "Invalid credentials"}), 401
