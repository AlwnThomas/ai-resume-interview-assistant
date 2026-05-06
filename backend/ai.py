from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_resume_text(resume_text: str, job_description: str):
    prompt = f"""
You are an expert ATS resume reviewer and technical recruiter.

Compare the resume against the job description.

Return:
1. Match score out of 100
2. Strong matches
3. Missing or weak skills
4. Resume improvement suggestions
5. Suggested rewritten bullet points
6. Keywords to add

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content