import requests

api_url = 'https://chat.openai.com/'

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Check for any HTTP errors
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
