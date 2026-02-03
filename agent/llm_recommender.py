import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_recommendation(metrics: dict, context: str) -> str:
    """
    Generate optimization recommendations using retrieved context
    """

    prompt = f"""
You are a senior Google Ads optimization expert.

Campaign Performance Metrics:
{metrics}

Relevant Best Practices and Knowledge:
{context}

Instructions:
- Identify key problems clearly
- Explain why they are happening
- Give 3–5 actionable optimization steps
- Keep recommendations practical and data-driven
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert performance marketing consultant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
