from flask import Flask, request, jsonify
import requests
import random
import time

app = Flask(__name__)

@app.route("/", methods=["GET"])
def send_email():
    email = request.args.get("email")
    count = request.args.get("count", default=1, type=int)

    if not email:
        return jsonify({
            "credit": "API OWNER BY: @hardhackar007",
            "status": "error",
            "message": "Missing 'email' parameter"
        }), 400

    url = "https://appbowl.com/api/sms/send-email"
    headers = {
        "Host": "appbowl.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Android\"",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "Accept": "*/*",
        "Origin": "https://appbowl.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://appbowl.com/",
        "Accept-Language": "en-US,en;q=0.9"
    }

    results = []
    for i in range(count):
        name = f"Alert-{random.randint(1000, 9999)}"
        data = {
            "name": name,
            "email": email
        }

        try:
            resp = requests.post(url, headers=headers, json=data, timeout=10)
            results.append({
                "count": i + 1,
                "name_used": name,
                "status_code": resp.status_code,
                "server_response": resp.text
            })
            time.sleep(1)  # 1 second delay
        except Exception as e:
            results.append({
                "count": i + 1,
                "error": str(e)
            })

    return jsonify({
        "credit": "API OWNER BY: @hardhackar007",
        "status": "success",
        "email_sent_to": email,
        "requests_sent": count,
        "results": results
    })
