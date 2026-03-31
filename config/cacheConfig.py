import time

cache = {}

def set_token(service, userId, hashToken, ttl=60):
    expire_at = time.time() + ttl
    cache[(service, userId, hashToken)] = {
        "token": hashToken,
        "ttl": ttl,
        "expire_at": expire_at
    }

def fetch_token(service, userId, hashToken):
    key = (service, userId, hashToken)
    if key in cache:
        data = cache[key]
        if time.time() < data["expire_at"]:
            return data
        else:
            del cache[key]
    return None
