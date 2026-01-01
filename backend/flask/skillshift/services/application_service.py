from extensions import db
from models import Resume, Application
from matcher import calculate_match

def create_application(user_id: int, company: str, role: str, job_description: str):
    resume = Resume.query.filter_by(user_id=user_id).first()

    if not resume:
        raise ValueError("No resume found for user")

    score = calculate_match(resume.resume_text, job_description)

    application = Application(
        user_id=user_id,
        company=company,
        role=role,
        job_description=job_description,
        match_score=score
    )

    db.session.add(application)
    db.session.commit()

    return application
