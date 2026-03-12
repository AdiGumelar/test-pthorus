from ..models import User
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(data):

    existing_user = User.query.filter_by(username=data["username"]).first()
    if existing_user:
        return None, "Username sudah digunakan"

    existing_email = User.query.filter_by(email=data["email"]).first()
    if existing_email:
        return None, "Email sudah digunakan"

    hashed_password = generate_password_hash(data["password"])

    user = User(
        username=data["username"],
        password=hashed_password,
        email=data["email"],
        nama=data["nama"]
    )

    db.session.add(user)
    db.session.commit()

    return user, None


def login_user(data):

    user = User.query.filter_by(username=data["username"]).first()

    if not user:
        return None

    if not check_password_hash(user.password, data["password"]):
        return None

    return user


def get_all_users(search=None):

    query = User.query

    if search:
        query = query.filter(
            (User.username.ilike(f"%{search}%")) |
            (User.nama.ilike(f"%{search}%"))
        )

    users = query.all()

    return [user.to_dict() for user in users]

def get_user_by_id(id):

    user = User.query.get(id)

    if not user:
        return None

    return user.to_dict()


def update_user(user_id, data):

    user = User.query.get(user_id)

    if not user:
        return False, "User tidak ditemukan"

    if "username" in data:
        existing_user = User.query.filter_by(username=data["username"]).first()

        if existing_user and existing_user.id != user_id:
            return False, "Username sudah digunakan"
    
    if "email" in data:
        existing_user = User.query.filter_by(username=data["email"]).first()

        if existing_user and existing_user.id != user_id:
            return False, "Email sudah digunakan"

    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.nama = data.get("nama", user.nama)

    db.session.commit()

    return True, "User berhasil diupdate"


def delete_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return False

    db.session.delete(user)
    db.session.commit()

    return True