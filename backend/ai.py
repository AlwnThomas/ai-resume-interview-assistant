from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_resume_text(resume_text: str):
    prompt = f"""
You are an expert resume reviewer.

Analyze this resume and return:
1. Overall score out of 100
2. Strengths
3. Weaknesses
4. Missing skills
5. Specific improvement suggestions

Resume:
{resume_text}
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