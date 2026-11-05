from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "message": "Order Service is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "order-service"
    }), 200

@app.route("/orders")
def orders():
    return jsonify([
        {"id": 1, "user_id": 1, "product": "Laptop", "quantity": 1},
        {"id": 2, "user_id": 2, "product": "Smartphone", "quantity": 2}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
