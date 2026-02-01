import requests  # Import the waiter

# 1. The URL (The Menu Item we want)
url = "https://jsonplaceholder.typicode.com/todos/1"

# 2. Send the Request (The Waiter goes to the kitchen)
print("Sending request to the internet...")
response = requests.get(url)

# 3. Check the Result
print("Status Code:", response.status_code) # 200 means "OK" (Success)

# 4. Parse the Data (Unpack the food)
data = response.json() 

print("\nHere is the data we got back:")
print(data)