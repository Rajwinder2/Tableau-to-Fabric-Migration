
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/health")
def health():
    return jsonify({"status": "Backend is running"})

@app.route("/api/migrate")
def migrate():
    return jsonify({
        "migrationId": "MIG-1001",
        "status": "IN_PROGRESS",
        "message": "Dummy migration started"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
