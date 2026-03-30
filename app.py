import streamlit as st
import pandas as pd
import pickle
import os
import pdfplumber
from ats_logic import calculate_ats_score

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer")
st.write("Upload your resume and get role prediction + ATS score")

# -----------------------------
# Load Model Safely
# -----------------------------

try:
    model_path = "models/models/model.pkl"
    tfidf_path = "models/models/tfidf.pkl"

    model = pickle.load(open(model_path, "rb"))
    tfidf = pickle.load(open(tfidf_path, "rb"))

except Exception as e:
    st.error("Model loading failed. Check model path.")
    st.stop()


# -----------------------------
# Resume Text Extraction
# -----------------------------

def extract_text_from_pdf(uploaded_file):
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text


# -----------------------------
# File Upload
# -----------------------------

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    st.success("Resume uploaded successfully")

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Resume Preview")
    st.write(resume_text[:1000])

    # -----------------------------
    # Role Prediction
    # -----------------------------

    vector = tfidf.transform([resume_text])

    prediction = model.predict(vector)[0]

    st.subheader("🎯 Predicted Job Role")
    st.success(prediction)

    # -----------------------------
    # Job Description Input
    # -----------------------------

    st.subheader("📄 Paste Job Description for ATS Score")

    job_description = st.text_area("Enter Job Description")

    if job_description:

        ats_score = calculate_ats_score(resume_text, job_description)

        st.subheader("📊 ATS Score")

        st.progress(ats_score / 100)

        st.write(f"ATS Score: **{ats_score}%**")

        if ats_score > 75:
            st.success("Great! Your resume matches the job well.")
        elif ats_score > 50:
            st.warning("Moderate match. Improve some skills.")
        else:
            st.error("Low match. Add more relevant keywords.")            
            



import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

