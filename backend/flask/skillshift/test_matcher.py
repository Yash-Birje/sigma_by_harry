from matcher import calculate_match
resume = """
Python developer with experience in Flask, SQLAlchemy,
machine learning, NLP, and backend systems.
"""

job = """
Looking for a backend engineer with strong Python skills,
experience in Flask, databases, and machine learning.
"""

print(calculate_match(resume, job))