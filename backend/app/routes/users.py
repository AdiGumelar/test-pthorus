from flask import Blueprint, request, jsonify
from ..services import (
    register_user,
    login_user,
    get_all_users,
    update_user,
    delete_user,
    get_user_by_id
)
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

user_bp = Blueprint("users", __name__)

@user_bp.route("/users/register", methods=["POST"])
def register():

    data = request.get_json()

    user, error = register_user(data)

    if error:
        return jsonify({"message": error}), 400

    return jsonify({
        "message": "Registrasi berhasil",
        "user": user.to_dict()
    }), 201

@user_bp.route("/users/login", methods=["POST"])
def login():

    data = request.get_json()

    user = login_user(data)

    if not user:
        return jsonify({"message": "Username atau password salah"}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "message": "Login berhasil",
        "token": access_token
    }), 200

@user_bp.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    search = request.args.get("search")
    users = get_all_users(search)

    return jsonify(users), 200

@user_bp.route("/users/<int:id>", methods=["GET"])
def get_user(id):

    user = get_user_by_id(id)

    if not user:
        return jsonify({"message": "User tidak ditemukan"}), 404

    return jsonify(user), 200

@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id):

    data = request.get_json()

    success = update_user(user_id, data)

    if not success:
        return jsonify({"message": "User tidak ditemukan"}), 404

    return jsonify({"message": "Data user berhasil diperbarui"}), 200

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id):

    success = delete_user(user_id)

    if not success:
        return jsonify({"message": "User tidak ditemukan"}), 404

    return jsonify({"message": "User berhasil dihapus"}), 200