from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        import models   # <-- IMPORTANT: import the module, not names
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)