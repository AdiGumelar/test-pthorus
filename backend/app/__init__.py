from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, cors
from .routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(user_bp)

    from .models import User

    return app