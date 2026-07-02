from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import razorpay
import os

app = Flask(__name__)
CORS(app)

client = razorpay.Client(auth=(
    os.environ.get("RAZORPAY_KEY_ID", "rzp_live_T8XptW4xmDFEIt"),
    os.environ.get("RAZORPAY_KEY_SECRET", "Ju6RopNVyXt1Fv57O4wktdOt")
))

@app.get("/")
def index():
    return send_from_directory(".", "index.html")

@app.get("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

@app.post("/create-order")
def create():
    order = client.order.create({
        "amount": 500,
        "currency": "INR",
        "payment_capture": 1
    })
    return jsonify(order)

@app.post("/verify")
def verify():
    data = request.json
    try:
        client.utility.verify_payment_signature(data)
        return jsonify({
            "success": True,
            "link": "https://t.me/YourPrivateChannelInvite"
        })
    except:
        return jsonify({"success": False}), 400

if __name__ == "__main__":
    app.run(debug=True)