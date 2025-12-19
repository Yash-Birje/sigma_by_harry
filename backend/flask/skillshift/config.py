import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / "instance" / ".env"
load_dotenv(env_path)

class Config:
    print("DB URL:", os.getenv("DATABASE_URL"))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")