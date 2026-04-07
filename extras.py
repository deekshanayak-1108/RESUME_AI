def fake_check(resume_text):
    suspicious_words = ["lorem ipsum", "fake", "dummy"]

    for word in suspicious_words:
        if word in resume_text.lower():
            return "⚠️ Suspicious Resume Detected"

    return "✅ Resume Looks Genuine"