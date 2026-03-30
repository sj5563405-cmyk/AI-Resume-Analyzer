def calculate_ats(resume_text, job_desc):

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_desc.lower().split())

    match = resume_words.intersection(jd_words)

    score = len(match)/len(jd_words) * 100

    return round(score,2)

