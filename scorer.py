def calculate_score(found_skills, required_skills):
    if not required_skills:
        return 0

    match_count = len(set(found_skills) & set(required_skills))
    score = (match_count / len(required_skills)) * 100

    return round(score, 2)