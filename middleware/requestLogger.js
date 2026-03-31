import datetime

def request_logger():
    now = datetime.datetime.now().isoformat()
    # Flask menyediakan objek request global
    from flask import request
    method = request.method
    path = request.path
    ip = request.remote_addr

    print(f"[{now}] {ip} {method} {path}")
