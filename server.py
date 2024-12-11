from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/generate-domains', methods=['POST'])
def generate_domains():
    data = request.get_json()
    input_text = data.get('text', '')

    # Komunikasi dengan Strvm/meta-ai-api
    prompt = f"Buatkan 10 nama domain tld .id dengan kombinasi dari beberapa kata {input_text}"
    response = requests.post(
        "http://api:8000/generate", 
        json={"prompt": prompt, "max_tokens": 100}
    )

    if response.status_code == 200:
        result = response.json()
        domains = result.get('choices', [{}])[0].get('text', '').split("\n")
        return jsonify({"domains": domains})
    else:
        return jsonify({"error": "Failed to fetch domains"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
