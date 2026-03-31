import datetime
from flask import request

def log_request():
    now = datetime.datetime.now().isoformat()
    method = request.method
    path = request.path
    ip = request.remote_addr
    print(f"[{now}] {ip} {method} {path}")
