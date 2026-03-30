# 🚀 AI Resume Analyzer

An intelligent **AI-powered Resume Analysis System** that evaluates resumes using **Machine Learning and Natural Language Processing**. The application extracts skills, predicts suitable job roles, calculates ATS compatibility with job descriptions, and provides feedback to improve resume quality.

The system also visualizes insights through charts and graphs, helping users understand their strengths and identify skill gaps required for specific job roles.

---

# 🎯 Project Objective

Many companies use **Applicant Tracking Systems (ATS)** to automatically filter resumes before they reach recruiters.

However, many candidates get rejected not because they lack skills, but because their resume is **not optimized for ATS systems**.

This project aims to build an **AI-based resume analysis tool** that:

* Evaluates resumes automatically
* Predicts the most suitable job role
* Calculates ATS compatibility
* Identifies missing skills
* Provides intelligent feedback for improvement

---

# 🧠 Key Features

### 📄 Resume Upload

Users can upload resumes in multiple formats:

* PDF Resume Upload
* Image Resume Upload (OCR text extraction)
* Manual Resume Text Input

---

### 🔎 Skill Extraction

The system analyzes resume text and detects **technical skills** using a predefined skills database.

Example detected skills:

* Python
* Machine Learning
* SQL
* Data Analysis
* Deep Learning

---

### 🔥 ATS Score Calculation

Users can paste a **Job Description**, and the system calculates how well the resume matches the job requirements.

The ATS score is calculated using keyword matching between:

Resume Content
Job Description

---

### 🧠 Resume Role Prediction (Machine Learning)

A trained **Machine Learning model** predicts the most suitable job role for the candidate based on resume content.

Example predictions:

* Data Scientist
* Data Analyst
* Python Developer
* Machine Learning Engineer
* Web Developer

---

### 📊 Skill Frequency Visualization

The application generates charts showing how frequently skills appear in the resume.

This helps understand **core technical strengths**.

---

### 📊 Skill Radar Chart

A radar chart visually represents candidate skills to give a **quick overview of technical capabilities**.

---

### 📉 Resume vs Job Skill Gap Analysis

The system compares:

Resume Skills
Job Description Skills

It identifies **missing skills required for the job role**.

---

### ☁ Word Cloud Visualization

A **WordCloud** visualizes the most important words in the resume to highlight key areas.

---

### ⭐ Resume Strength Score

The system calculates an overall **Resume Strength Score** based on:

* Skills presence
* Resume structure
* ATS compatibility

---

### 🤖 AI Resume Feedback

The system provides intelligent suggestions such as:

* Add more technical skills
* Include project experience
* Add measurable achievements
* Improve resume structure

---

# 🛠 Technologies Used

Programming Language:

* Python

Libraries and Tools:

* Streamlit (Web Application Framework)
* Pandas (Data Processing)
* Scikit-learn (Machine Learning)
* Matplotlib (Data Visualization)
* WordCloud (Text Visualization)
* PDFPlumber (PDF Text Extraction)
* Pytesseract (OCR for Image Resumes)

---

# 🧠 Machine Learning Workflow

The resume role prediction model was trained using the following steps:

1. Dataset preprocessing
2. Text cleaning and normalization
3. Feature extraction using **TF-IDF Vectorization**
4. Training classification model
5. Saving model using **Pickle**

The trained model predicts job roles based on resume content.

---

# 📂 Project Structure

AI-Resume-Analyzer

app.py – Main Streamlit application
train_model.py – Machine learning model training
ats_logic.py – ATS score calculation logic
skills_db.py – Skill keyword database
requirements.txt – Python dependencies
UpdatedResumeDataSet.csv – Training dataset

models/

model.pkl – Trained machine learning model
tfidf.pkl – TF-IDF vectorizer

---

# ▶ How to Run the Project

Step 1 – Clone the repository

git clone https://github.com/your-username/AI-Resume-Analyzer.git

Step 2 – Navigate to project folder

cd AI-Resume-Analyzer

Step 3 – Install dependencies

pip install -r requirements.txt

Step 4 – Run the application

streamlit run app.py

---

# 🌐 Live Application

The project is deployed using **Streamlit Cloud**.

Live App Link:

(Add your deployed Streamlit link here)

---

# 📈 Future Improvements

Possible future improvements include:

* LLM-powered resume feedback
* Resume chatbot for career guidance
* Semantic ATS scoring using embeddings
* Automatic resume rewriting suggestions
* More advanced NLP analysis

---

# 👨‍💻 Author

Harshal Jadhav

AI / Data Analytics Enthusiast
Interested in Machine Learning, Data Science and AI-powered applications.

---

# ⭐ Project Summary

AI Resume Analyzer demonstrates how **Machine Learning, NLP, and Data Visualization** can be combined to build an intelligent system that helps job seekers optimize their resumes and improve job matching.

This project showcases practical implementation of **AI in real-world career tools**.
