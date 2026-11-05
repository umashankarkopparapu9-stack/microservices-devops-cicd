from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "message": "User Service is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "user-service"
    }), 200

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Shankar"},
        {"id": 2, "name": "DevOps User"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
