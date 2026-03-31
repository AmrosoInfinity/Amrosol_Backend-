import requests

GIST_URLS = {
    "grab": "https://gist.githubusercontent.com/AmrosoInfinity/5b19fdb53aa1bfcfa4fc3843165b9471/raw/Grab",
    "gojek": "https://gist.githubusercontent.com/AmrosoInfinity/aebd0ba65e12a20b062c291c68714d8a/raw/Gojek"
}

def fetch_tokens_from_gist(service: str):
    """Ambil token dari gist sesuai service."""
    url = GIST_URLS[service]
    res = requests.get(url, timeout=5)
    return [line.strip() for line in res.text.splitlines() if line.strip()]
