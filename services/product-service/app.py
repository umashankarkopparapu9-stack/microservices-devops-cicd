from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "message": "Product Service is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "product-service"
    }), 200

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 55000},
        {"id": 2, "name": "Smartphone", "price": 25000},
        {"id": 3, "name": "Headphones", "price": 2000}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
