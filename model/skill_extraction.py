import spacy

nlp = spacy.load("en_core_web_sm")

SKILL_DB = [
    "python", "java", "c++", "machine learning", "deep learning",
    "sql", "mongodb", "tensorflow", "pandas", "numpy",
    "aws", "docker", "kubernetes", "git", "linux"
]

def extract_skills(text):
    text_lower = text.lower()
    extracted_skills = []   

    for skill in SKILL_DB:
        if skill in text_lower:
            extracted_skills.append(skill)

    return list(set(extracted_skills))
