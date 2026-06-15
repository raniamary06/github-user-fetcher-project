import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

username = input("Enter the Username: ")
url = f"https://api.github.com/users/{username}"

if TOKEN:
    headers = {"Authorization":f"Bearer {TOKEN}"}
else:
    print("Warning: No token found. Proceeding with unauthenticated request.")
    headers = {}

response = requests.get(url, headers = headers)

if response.status_code == 404: 
    print(f"Error: Github user '{username}' not found")

elif response.status_code != 200:
    print(f"Error {response.status_code}: {response.json().get('message')}")

else:
    data = response.json()
    created_at_raw = data.get("created_at")
    created_at = datetime.strptime(created_at_raw, "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y")

    print("\n===== GitHub User Info =====")
    print(f"Name: {data.get('name')}")
    print(f"Username: {data.get('login')}")
    print(f"Bio: {data.get('bio')}")
    print(f"Followers: {data.get('followers')}")
    print(f"Following: {data.get('following')}")
    print(f"Public Repos: {data.get('public_repos')}")
    print(f"Account Created on: {created_at}")


    repos_url = f"https://api.github.com/users/{username}/repos?sort=stars&per_page=5"
    repos_response = requests.get(repos_url, headers=headers)

    if repos_response.status_code == 200:
        repos = repos_response.json()
        print("\n===== Top 5 Repositories =====")
        for i,repo in enumerate(repos,start=1):
            print(f"{i}. {repo['name']}")
    
    else:
        print("Could not fetch repos.")
