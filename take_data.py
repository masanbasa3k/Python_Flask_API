import requests

# Replace this with your API endpoint URL
api_url = 'http://127.0.0.1:5000/api/data'

# Replace this with your actual secret key
secret_key = input("Enter your secret key: ")

# Include the secret key in the headers as an Authorization token
headers = {
    'Authorization': secret_key
}

try:
    # Send a GET request to the API endpoint with the token in the headers
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print("Data received:")
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
