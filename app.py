from flask import Flask
import openai
import os

app = Flask(__name__)

# Загружаем API ключ из переменных среды Render
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Привет, мир!"

@app.route("/test")
def test():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Скажи тестовое сообщение"}],
            max_tokens=20
        )
        return f"✅ OpenAI API работает! Ответ: {response.choices[0].message['content']}"
    except Exception as e:
        return f"❌ Ошибка: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
