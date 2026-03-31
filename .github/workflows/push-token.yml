name: Push Token to Web

on:
  workflow_dispatch:
    inputs:
      service:
        description: "Service name"
        required: true
      userId:
        description: "User ID"
        required: true

jobs:
  generate-and-push:
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

      - name: Run generator
        run: python generate.py ${{ github.event.inputs.service }} ${{ github.event.inputs.userId }}

      - name: Checkout web repo
        uses: actions/checkout@v3
        with:
          repository: AmrosoInfinity/Amrosol-Website
          token: ${{ secrets.FRONTEND_TOKEN }}
          path: web

      - name: Copy generated tokens
        run: cp -r token/* web/tokens/

      - name: Commit & push
        run: |
          cd web
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add .
          git commit -m "Update token for ${{ github.event.inputs.service }} user ${{ github.event.inputs.userId }}"
          git push
