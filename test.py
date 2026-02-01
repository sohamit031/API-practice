import requests

try:
    print("Attempting to connect to Google...")
    response = requests.get("https://www.google.com", timeout=5)
    print(f"✅ Success! Status Code: {response.status_code}")
    print("Your Python CAN access the internet.")
except Exception as e:
    print(f"❌ Failed: {e}")
    print("Your Python is BLOCKED from the internet completely.")