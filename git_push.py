import subprocess, os

def push_to_frontend_repo(service, user_id, hash_token):
    gh_pat = os.getenv("FRONTEND_TOKEN")
    repo_url = f"https://{gh_pat}@github.com/AmrosoInfinity/Amrosol-website.git"

    # Set remote dengan PAT
    subprocess.run(["git", "remote", "set-url", "origin", repo_url], check=True)

    # Add, commit, push
    subprocess.run(["git", "add", "tokens/"], check=True)
    subprocess.run(["git", "commit", "-m", f"Add token page for {service}/{user_id}/{hash_token}"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
