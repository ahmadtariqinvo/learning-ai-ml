from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

MODEL = "openai/gpt-4o-mini"


def ask_llm(system_prompt, user_prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {e}"


def extract_data(raw_text):
    return ask_llm(
        "You are a data extraction assistant. Return ONLY valid JSON.",
        f"""
Extract:

{{
  "name": "",
  "email": "",
  "phone": ""
}}

Text:
{raw_text}
"""
    )


result = extract_data(
    "my name is ahmad tariq where my email is ahmad@ahmad.com and number is 0308978777897"
)

print(result)
print(type(result))

data = json.loads(result)
print(type(data))
