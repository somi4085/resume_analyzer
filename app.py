from fastapi import FastAPI, UploadFile, File, Form

from utils.parser import extract_text_from_pdf
from model.preprocessing import clean_text
from model.features import vectorize
from model.similarity import get_match_Score
from model.skill_extraction import extract_skills
from model.missing_skill import get_missing_skills
from model.ai_suggestions import generator_summarizer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Analyzer Running 🚀"}


@app.post("/analyze")
async def analyze(file: UploadFile = File(...), jd: str = Form(...)):

    # Extract
    resume_text = extract_text_from_pdf(file.file)

    # Clean
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd)

    # Vector + Score
    vectors = vectorize(resume_clean, jd_clean)
    match_score = get_match_Score(vectors)

    # Skills
    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)

    # Missing skills (FIXED)
    missing_skills = get_missing_skills(resume_skills, jd_skills)

    # AI
    suggestions = generator_summarizer(resume_text)

    return {
        "match_score": match_score,   # ✅ FIXED
        "resume_skills": resume_skills,   # ✅ FIXED
        "jd_skills": jd_skills,           # ✅ FIXED
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }

