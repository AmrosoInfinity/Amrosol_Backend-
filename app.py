from flask import Flask, request, jsonify
import hashlib, random, time, json

app = Flask(__name__)

TOKENS = {
    "grab": ["grabToken1", "grabToken2", "grabToken3"],
    "gojek": ["gojekToken1", "gojekToken2", "gojekToken3"]
}

TTL_DEFAULT = 60  # detik

@app.route("/generate", methods=["POST"])
def generate_token():
    data = request.json
    service = data.get("service")
    user_id = str(data.get("userId"))

    if service not in TOKENS:
        return jsonify({"error": "Service tidak valid"}), 400

    chosen = random.choice(TOKENS[service])
    hash_token = hashlib.sha256(chosen.encode()).hexdigest()[:16]
    expire_at = int(time.time()) + TTL_DEFAULT

    token_data = {
        "service": service,
        "userId": user_id,
        "token": chosen,
        "hashToken": hash_token,
        "ttl": f"{TTL_DEFAULT} detik",
        "expire_at": expire_at
    }

    # Simpan ke file JSON untuk frontend
    with open("token.json", "w") as f:
        json.dump(token_data, f)

    # URL sesuai format service/user_id/hash_token
    url = f"https://amrosol.online/{service}/{user_id}/{hash_token}"
    return jsonify({"url": url, "token": token_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
