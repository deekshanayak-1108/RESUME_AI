import streamlit as st
from skills import extract_skills
from scorer import calculate_score
from gap import find_missing
from extras import fake_check

st.title("AI Resume Screening System")

# Input resume
resume_text = st.text_area("Paste Resume Text")

# Input required skills
required_skills_input = st.text_input("Enter Required Skills (comma separated)")

if st.button("Analyze Resume"):
    if resume_text and required_skills_input:

        required_skills = [skill.strip().lower() for skill in required_skills_input.split(",")]

        # Process
        found_skills = extract_skills(resume_text)
        score = calculate_score(found_skills, required_skills)
        missing_skills = find_missing(found_skills, required_skills)
        authenticity = fake_check(resume_text)

        # Output
        st.subheader("Results")

        st.write("**Extracted Skills:**", found_skills)
        st.write("**Match Score:**", f"{score}%")
        st.write("**Missing Skills:**", missing_skills)
        st.write("**Authenticity Check:**", authenticity)

    else:
        st.warning("Please enter resume text and required skills")
