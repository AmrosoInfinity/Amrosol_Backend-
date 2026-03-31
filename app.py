from flask import Flask, request, jsonify
import hashlib, random, time, json
import requests

app = Flask(__name__)

# URL gist untuk masing-masing service
GIST_URLS = {
    "grab": "https://gist.githubusercontent.com/AmrosoInfinity/5b19fdb53aa1bfcfa4fc3843165b9471/raw/Grab",
    "gojek": "https://gist.githubusercontent.com/AmrosoInfinity/aebd0ba65e12a20b062c291c68714d8a/raw/Gojek"
}

TTL_DEFAULT = 60  # detik

def fetch_tokens_from_gist(service):
    url = GIST_URLS.get(service)
    if not url:
        return []
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            # gist biasanya berisi token per baris
            return [line.strip() for line in res.text.splitlines() if line.strip()]
    except Exception as e:
        print(f"Error fetch gist {service}: {e}")
    return []

@app.route("/generate", methods=["POST"])
def generate_token():
    data = request.json
    service = data.get("service")
    user_id = str(data.get("userId"))

    tokens = fetch_tokens_from_gist(service)
    if not tokens:
        return jsonify({"error": "Token tidak ditemukan"}), 404

    chosen = random.choice(tokens)
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
