from flask import Flask
from openai import OpenAI
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask-приложение работает на Render!"

@app.route("/test")
def test_openai():
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.responses.create(
            model="gpt-5",
            input="Say: Hello from OpenAI test!"
        )
        return response.output[0].content[0].text
    except Exception as e:
        return f"❌ Ошибка при обращении к OpenAI: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
