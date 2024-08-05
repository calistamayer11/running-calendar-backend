from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("open_ai_key")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a cross country coach. You are providing to the users a running mileage training plan.",
        },
        {"role": "user", "content": "Give me a training plan."},
    ],
)

print(completion.choices[0].message)
