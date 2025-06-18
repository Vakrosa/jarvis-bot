from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8078991244:AAFmM1okdqfncLGrk9kdRYDDBRCgubLovKc"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": f"Ви написали: {text}"}
    headers = {"Content-Type": "application/json"}
    requests.post(url, json=payload, headers=headers)

@app.route("/telegram-webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    print("✅ Отримано:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        send_message(chat_id, text)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


