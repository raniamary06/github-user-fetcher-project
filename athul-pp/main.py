#libraries
import requests

#Initialising the function to get the username from the user
def get_github_user():
    username = input("Enter your username: ")
    api_url  = f"https://api.github.com/users/{username}"

    print(f"\nFetching data for {username}...\n")

    response = requests.get(api_url)

    if response.status_code == 200:
        user_data = response.json() 
        
        name       = user_data.get("name")
        login      = user_data.get("login") 
        bio        = user_data.get("bio")
        followers  = user_data.get("followers")
        following  = user_data.get("following")
        repos      = user_data.get("public_repos")
        created_at = user_data.get("created_at")

        print("-" * 30)
        print(f"Name: {name}")
        print(f"Username: {login}")
        print(f"Bio: {bio}")
        print(f"Followers: {followers} | Following: {following}")
        print(f"Public Repositories: {repos}")
        print(f"Account Created: {created_at}")
        print("-" * 30)

    elif response.status_code == 404:
        print(f"Error: {username} does not exist on GitHub.")
    else:
        print(f"Error: Something went wrong. Error Status Code: {response.status_code}")


# This tells Python to run our function when the script starts
if __name__ == "__main__":
    get_github_user()