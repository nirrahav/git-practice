import requests

def get_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        data = response.json()
        print(f"{data['setup']}")
        print(f"{data['punchline']}")
    else:
        print("Couldn't fetch a joke right now 😅")
def greeting():
    print("Welcome to the joke!")
if __name__ == "__main__":
    print("Fetching a random joke for you...\n")
    get_random_joke()
