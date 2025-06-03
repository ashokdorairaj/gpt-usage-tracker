from flask import Flask, request, send_file
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/log-gpt-usage", methods=["POST"])
def log_usage():
    data = request.json
    log_entry = f"{datetime.utcnow().isoformat()} - {data}\n"
    with open("usage_log.txt", "a") as log_file:
        log_file.write(log_entry)
    return {"status": "logged"}, 200

@app.route("/openapi.yaml", methods=["GET"])
def serve_openapi():
    return send_file("openapi.yaml", mimetype="text/yaml")

if __name__ == "__main__":
    app.run(debug=False, port=int(os.environ.get("PORT", 8080)), host="0.0.0.0")
