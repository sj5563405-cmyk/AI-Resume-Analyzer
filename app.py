import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pdfplumber
import pytesseract
from PIL import Image
from collections import Counter
import numpy as np
import pickle
from wordcloud import WordCloud
from skills_db import skills_list

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# ---------------- UI STYLE ----------------

st.markdown("""
<style>

.stApp{
background-color:#0f172a;
color:white;
}

section[data-testid="stSidebar"]{
background-color:#111827;
color:white;
}

label{
color:white !important;
}

textarea,input{
background-color:#1f2937 !important;
color:white !important;
}

[data-testid="stMetricValue"]{
color:white !important;
font-size:28px;
}

[data-testid="stMetricLabel"]{
color:#9ca3af !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🚀 AI Resume Analyzer")
st.write("Upload resume to analyze skills, ATS compatibility, and role prediction.")

# ---------------- LOAD MODEL ----------------

model = pickle.load(open("models/models/model.pkl","rb"))
tfidf = pickle.load(open("models/models/tfidf.pkl","rb"))

# ---------------- SIDEBAR ----------------

st.sidebar.header("Resume Input")

input_type = st.sidebar.selectbox(
"Choose Resume Input",
["Upload PDF","Upload Image","Paste Resume"]
)

job_desc = st.sidebar.text_area("Paste Job Description (optional)")

# ---------------- TEXT EXTRACTION ----------------

def extract_pdf(file):

    text=""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content

    return text


def extract_image(file):

    st.warning("Image OCR is disabled in cloud deployment. Please upload PDF instead.")

    return ""


# ---------------- INPUT ----------------

resume_text=""

if input_type=="Upload PDF":

    pdf_file = st.file_uploader("Upload Resume PDF")

    if pdf_file:
        resume_text = extract_pdf(pdf_file)

elif input_type=="Upload Image":

    img_file = st.file_uploader("Upload Resume Image")

    if img_file:
        resume_text = extract_image(img_file)

else:

    resume_text = st.text_area("Paste Resume Text")


# ---------------- MAIN ANALYSIS ----------------

if resume_text:

    resume_lower = resume_text.lower()

    # Resume preview cleaner
    with st.expander("📄 View Resume Text"):
        st.write(resume_text)

    # ---------------- SKILL EXTRACTION ----------------

    found_skills=[]

    for skill in skills_list:

        count = resume_lower.count(skill)

        if count>0:
            found_skills.extend([skill]*count)

    unique_skills=list(set(found_skills))

    st.subheader("🧠 Extracted Skills")

    st.markdown(", ".join(unique_skills))

    # ---------------- ROLE PREDICTION ----------------

    st.subheader("🧠 Predicted Job Role")

    vector = tfidf.transform([resume_text])

    prediction = model.predict(vector)[0]

    st.success(f"Predicted Role: {prediction}")

    # ---------------- ATS SCORE ----------------

    ats_score=0

    if job_desc:

        resume_words = set(resume_lower.split())
        jd_words = set(job_desc.lower().split())

        match = resume_words.intersection(jd_words)

        ats_score = (len(match)/len(jd_words))*100

        ats_score = round(ats_score,2)

        st.subheader("🔥 ATS Score")

        st.metric("ATS Score",str(ats_score)+"%")

        if ats_score>80:
            grade="A"
        elif ats_score>60:
            grade="B"
        elif ats_score>40:
            grade="C"
        else:
            grade="D"

        st.metric("Resume Grade",grade)

    # ---------------- SKILL FREQUENCY ----------------

    st.subheader("📈 Skill Frequency")

    skill_counts = Counter(found_skills)

    df = pd.DataFrame({
        "Skill":list(skill_counts.keys()),
        "Count":list(skill_counts.values())
    })

    fig, ax = plt.subplots()

    ax.bar(df["Skill"],df["Count"])

    plt.xticks(rotation=45)

    st.pyplot(fig)

    # ---------------- RADAR CHART ----------------

    st.subheader("📊 Skill Radar Chart")

    radar_skills = unique_skills[:6]

    if len(radar_skills)>0:

        values=[1]*len(radar_skills)

        angles=np.linspace(0,2*np.pi,len(radar_skills),endpoint=False)

        fig2 = plt.figure()

        ax2 = fig2.add_subplot(111, polar=True)

        ax2.plot(angles,values)

        ax2.fill(angles,values,alpha=0.3)

        ax2.set_xticks(angles)

        ax2.set_xticklabels(radar_skills)

        st.pyplot(fig2)

    # ---------------- SKILL GAP ----------------

    if job_desc:

        st.subheader("📉 Resume vs Job Skill Gap")

        jd_skills=[]

        for skill in skills_list:

            if skill in job_desc.lower():
                jd_skills.append(skill)

        missing=list(set(jd_skills)-set(unique_skills))

        st.write("Required Skills:",jd_skills)
        st.write("Missing Skills:",missing)

    # ---------------- WORDCLOUD ----------------

    st.subheader("☁ Resume WordCloud")

    wc = WordCloud(width=800,height=400,background_color="black").generate(resume_text)

    fig3, ax3 = plt.subplots()

    ax3.imshow(wc)

    ax3.axis("off")

    st.pyplot(fig3)

    # ---------------- RESUME STRENGTH SCORE ----------------

    st.subheader("⭐ Resume Strength Score")

    skills_score = min(len(unique_skills)*10,100)

    structure_score = 50

    if "experience" in resume_lower:
        structure_score += 20

    if "project" in resume_lower:
        structure_score += 20

    if "education" in resume_lower:
        structure_score += 10

    if ats_score == 0:
        final_score = (skills_score + structure_score)/2
    else:
        final_score = (skills_score + ats_score + structure_score)/3

    final_score = round(final_score,2)

    st.metric("Final Resume Score",str(final_score)+"%")

    # ---------------- AI FEEDBACK ----------------

    st.subheader("🤖 AI Resume Feedback")

    feedback=[]

    if len(unique_skills)<6:
        feedback.append("Add more technical skills.")

    if "project" not in resume_lower:
        feedback.append("Add projects section.")

    if "experience" not in resume_lower:
        feedback.append("Add experience section.")

    if "achievement" not in resume_lower:
        feedback.append("Add measurable achievements.")

    if len(feedback)==0:
        st.success("Resume looks strong!")

    else:
        for f in feedback:
            st.warning(f)


            




