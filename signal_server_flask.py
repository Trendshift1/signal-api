from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
signal_file = "signal.json"

@app.route("/signal", methods=["GET"])
def get_signal():
    if not os.path.exists(signal_file):
        return jsonify({"error": "No signal found"}), 404
    with open(signal_file, "r") as f:
        return jsonify(json.load(f))

@app.route("/signal", methods=["POST"])
def post_signal():
    try:
        new_signal = request.get_json(force=True)
        with open(signal_file, "w") as f:
            json.dump(new_signal, f, indent=4)
        return jsonify({"status": "updated", "signal_id": new_signal.get("trade_id", "unknown")})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
