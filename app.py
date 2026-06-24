from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/revenue")
def revenue():
    return jsonify({
        "total_revenue": 150000
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)