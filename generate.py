import os
import sys
from datetime import datetime

def main():
    # Ambil argumen service dan userId dari workflow dispatch
    if len(sys.argv) < 3:
        print("Usage: python generate.py <service> <userId>")
        sys.exit(1)

    service = sys.argv[1]
    user_id = sys.argv[2]

    # Pastikan folder token ada
    os.makedirs("token", exist_ok=True)

    # Nama file output
    filename = f"token/{service}_{user_id}.html"

    # Isi HTML sederhana
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Token {service} - {user_id}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f9f9f9;
            color: #333;
            text-align: center;
            padding: 50px;
        }}
        .box {{
            border: 2px solid #4CAF50;
            padding: 20px;
            background: #fff;
            display: inline-block;
        }}
    </style>
</head>
<body>
    <div class="box">
        <h1>Token {service.title()}</h1>
        <p>User ID: {user_id}</p>
        <p>Generated at: {datetime.utcnow().isoformat()} UTC</p>
        <p><strong>Token:</strong> {service}_{user_id}_TOKEN_PLACEHOLDER</p>
    </div>
</body>
</html>
"""

    # Tulis file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Generated token file: {filename}")

if __name__ == "__main__":
    main()
