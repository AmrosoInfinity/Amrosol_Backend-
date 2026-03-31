from services.token_cache import fetch_token

def get_token(service, userId, hashToken):
    token_data = fetch_token(service, userId, hashToken)
    if token_data:
        return {
            "service": service,
            "userId": userId,
            "hashToken": hashToken,
            "token": token_data["token"],
            "ttl": f"{token_data['ttl']} detik",
            "expire_at": token_data["expire_at"]
        }
    return None
