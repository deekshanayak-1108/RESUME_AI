import re

# Simple predefined skills list
SKILLS_DB = [
    "python", "java", "sql", "machine learning",
    "data analysis", "deep learning", "excel",
    "communication", "teamwork"
]

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if re.search(r'\b' + re.escape(skill) + r'\b', resume_text):
            found_skills.append(skill)

    return found_skills