from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise Exception("OPENROUTER_API_KEY not found")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "What is an LLM?"
        }
    ]
)

print(response.choices[0].message.content)