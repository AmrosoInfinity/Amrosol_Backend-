import os, sys, hashlib
from datetime import datetime
from utils.token_utils import fetch_tokens_from_gist

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate.py <service> <userId>")
        sys.exit(1)

    service = sys.argv[1]
    user_id = sys.argv[2]

    os.makedirs("token", exist_ok=True)

    # Ambil semua token dari gist
    tokens = fetch_tokens_from_gist(service)

    # Logika pemilihan token: misalnya pakai userId sebagai index
    try:
        index = int(user_id) % len(tokens)
        token_value = tokens[index]
    except Exception:
        token_value = "TOKEN_NOT_FOUND"

    # Hash untuk URL unik
    hash_token = hashlib.sha256(token_value.encode()).hexdigest()[:12]

    filename = f"token/{service}_{user_id}_{hash_token}.html"
    url = f"https://amrosol.online/{service}/{user_id}/{hash_token}.html"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Token {service} - {user_id}</title></head>
<body>
    <h1>Token {service.title()}</h1>
    <p>User ID: {user_id}</p>
    <p>Generated at: {datetime.utcnow().isoformat()} UTC</p>
    <p><strong>Token:</strong> {token_value}</p>
    <p>URL: <a href="{url}">{url}</a></p>
</body>
</html>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Generated token file: {filename}")
    print(f"Public URL: {url}")

if __name__ == "__main__":
    main()
