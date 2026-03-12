import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")
    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost/horus_gumelar_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False