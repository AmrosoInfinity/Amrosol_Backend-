name: Push Token to Web

on:
  workflow_dispatch:   # bisa dipicu manual atau lewat API dispatch
  push:
    paths:
      - "token/**"     # kalau ada perubahan di folder token

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout backend repo
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Generate token HTML
        run: python generate.py

      - name: Checkout web repo
        uses: actions/checkout@v3
        with:
          repository: AmrosoInfinity/Amrosol-Website
          token: ${{ secrets.FRONTEND_TOKEN }}
          path: web

      - name: Copy generated tokens
        run: cp -r token/* web/tokens/

      - name: Commit & push to web repo
        run: |
          cd web
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add .
          git commit -m "Update tokens from backend"
          git push
