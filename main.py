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
            "content": """You are a cross country coach. You are providing to the users a running mileage training plan.
            Please give responses as a JSON array of events such as the following:
            [
                {
                title  : 'event1',
                start  : '2010-01-01'
                },
                {
                title  : 'event2',
                start  : '2010-01-05',
                end    : '2010-01-07'
                },
                {
                title  : 'event3',
                start  : '2010-01-09T12:30:00',
                allDay : false // will make the time show
                }
            ]
            
            
            """,
        },
        {"role": "user", "content": "Give me a training plan."},
    ],
)

print(completion.choices[0].message)
