from services.token_cache import fetch_token

def get_token(service, userId, hashToken):
    return fetch_token(service, userId, hashToken)
