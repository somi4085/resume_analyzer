from transformers import pipeline

generator = pipeline(
    "text-generation",
    model = "gpt2"
)

def generator_summarizer(resume_text):
    prompt = f"""
    Analyze this resume and suggested improvement {resume_text}
"""
    result = generator(prompt, max_length=150, num_return_sequences=1)

    return result[0]["generated_text"]