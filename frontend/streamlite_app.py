import streamlit as st
import requests

# API endpoint
API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get insights 🚀")

# Upload resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description
jd = st.text_area("Paste Job Description")

# Button
if st.button("Analyze Resume"):

    if resume_file and jd:
        files = {"file": resume_file.getvalue()}
        data = {"jd": jd}

        with st.spinner("Analyzing..."):
            response = requests.post(API_URL, files=files, data=data)

        if response.status_code == 200:
            result = response.json()

            # 🎯 Display Results
            st.success("Analysis Complete ✅")

            # Match Score
            st.subheader("📊 Match Score")
            score = float(result["match_score"])
            st.progress(score / 100)
            st.write(f"score: {score}%")

            # Skills
            st.subheader("🧠 Skills")
            st.write("**Resume Skills:**", result["resume_skills"])
            st.write("**JD Skills:**", result["jd_skills"])

            # Missing Skills
            st.subheader("⚠️ Missing Skills")
            st.write(result["missing_skills"])

            # AI Suggestions
            st.subheader("🤖 AI Suggestions")
            st.write(result["suggestions"])

        else:
            st.error("Something went wrong ❌")

    else:
        st.warning("Please upload resume and enter job description")