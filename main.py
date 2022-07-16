from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def main():
    data = {
        "code": 50000,
        "message": "False",
    }
    return jsonify(data)