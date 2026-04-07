def find_missing(found_skills, required_skills):
    missing = list(set(required_skills) - set(found_skills))
    return missing