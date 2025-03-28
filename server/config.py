from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = os.getenv("FLASK_ENV") == "development"
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False