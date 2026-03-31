import time
from config.cache_config import TTL_DEFAULT, TTL_SERVICE

cache = {}

def set_token(service, userId, hashToken, token):
    ttl = TTL_SERVICE.get(service, TTL_DEFAULT)
    expire_at = time.time() + ttl
    cache[(service, userId, hashToken)] = {
        "token": token,
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
