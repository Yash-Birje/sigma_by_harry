from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    resumes = db.relationship("Resume", backref="user", lazy=True)
    applications = db.relationship("Application", backref="user", lazy=True)


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    resume_text = db.Column(db.Text, nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    company = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    job_description = db.Column(db.Text, nullable=False)

    match_score = db.Column(db.Float)
    status = db.Column(db.String(50), default="applied")
    applied_date = db.Column(db.DateTime, default=datetime.utcnow)
