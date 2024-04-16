from flask import Flask, request, jsonify, render_template
import requests
import json
import subprocess
app = Flask(__name__, template_folder='../client/src')

@app.route("/")
def home():
    return render_template("/index.html")

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/abi")
def get_abi():
    contract_address = request.args.get("address")
    if not contract_address:
        return jsonify({"error": "Contract address is required"}), 400
    
    try:
        response = requests.get(f"{ABI_ENDPOINT}{contract_address}")
        response_json = response.json()
        abi_json = json.loads(response_json.get("result", ""))
        return jsonify({"abi": abi_json})
    except Exception as e:
        return jsonify({"error": f"Error fetching ABI:{str(e)}"}), 500

@app.route("/fuzz")
def fuzz_contract():
    data = request.get_json()
    contractAddress = data['contractAddress']
    contractABI = data['contractABI']
    contractLanguage = data['contractLanguage']
    return jsonify({"message": "Fuzzing started"}), 200


if __name__ == "__main__":
    app.run(port=5000)