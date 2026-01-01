from extensions import db
from models import Resume

def save_or_replace_resume(user_id: int, resume_text: str):
    # delete existing resume (if any)
    Resume.query.filter_by(user_id=user_id).delete()

    new_resume = Resume(
        user_id=user_id,
        resume_text=resume_text
    )

    db.session.add(new_resume)
    db.session.commit()