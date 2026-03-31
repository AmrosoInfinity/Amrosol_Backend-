import hashlib, random, os
from utils.token_utils import fetch_tokens_from_gist
from git_push import push_to_frontend_repo

WEB_BASE = "https://amrosol.online"

def generate_token(service: str, user_id: str):
    tokens = fetch_tokens_from_gist(service)
    chosen = random.choice(tokens)

    hash_token = hashlib.sha256(chosen.encode()).hexdigest()[:16]

    folder = f"./tokens/{service}/{user_id}"
    os.makedirs(folder, exist_ok=True)
    filepath = f"{folder}/{hash_token}.html"

    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head><meta charset="UTF-8"><title>Token {service}</title></head>
<body>
<h2>Token {service.capitalize()}</h2>
<p id="token">{chosen}</p>
<button onclick="navigator.clipboard.writeText(document.getElementById('token').innerText)">Salin</button>
</body></html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Push ke repo frontend (GitHub Pages)
    push_to_frontend_repo(service, user_id, hash_token)

    return f"{WEB_BASE}/{service}/{user_id}/{hash_token}"
