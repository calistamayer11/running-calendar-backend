from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, send_from_directory
import json

app = Flask(__name__, static_folder='running_calendar_project', static_url_path='')

load_dotenv()
api_key = os.getenv("open_ai_key")

client = OpenAI(api_key=api_key)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/training-plan", methods=["GET"])
def get_training_plan():
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """You are a cross country coach. 
                    You are providing to the users a running mileage training plan for daily runs for one month.
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

        message_content = completion.choices[0].message.content
        print("Raw API response:", message_content)

        cleaned_content = message_content.strip().replace("```json", "").replace("```", "")
        events = json.loads(cleaned_content)

        return jsonify(events)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
