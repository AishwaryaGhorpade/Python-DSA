"""Requests Module in Python – Complete & Easy Explanation

The requests module is a popular third-party Python library used to send HTTP requests easily.

It is mainly used for:

Calling APIs

Fetching data from websites

Sending data to servers (forms, JSON, files)

Authentication & headers handling

1️⃣ Why Use requests?

Before requests, Python’s built-in "urllib" module was there for HTTP requests.:Hard to read 😖,Verbose and Less intuitive

requests makes HTTP simple and readable ✅"""

import requests
response = requests.get("https://api.example.com")
print(response.status_code)
# Output: 200
# requests provides a simple API for making HTTP requests with less code and better readability.

# 2️⃣ Installation
# pip install requests


# Check version:

print(requests.__version__)

"""
3️⃣ HTTP Methods Supported
HTTP Method	Purpose
GET	Fetch data
POST	Send data
PUT	Update data
DELETE	Remove data
PATCH	Partial update
HEAD	Headers only
4️⃣ GET Request (Most Common)"""

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.text)
# Output: (example)
# {
#   "userId": 1,
#   "id": 1,        
#   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#   "body": "quia et suscipit\nsuscipit..."
# } 

"""Important response attributes
response.status_code     # 200
response.text            # string response
response.json()          # JSON → dict
response.headers         # response headers
response.url             # final URL"""

# 5️⃣ Handling JSON Response
# ✔ Converts JSON → Python dictionary
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")   #response will get JSON data
data = response.json()  
print(data["title"])


# 6️⃣ POST Request (Sending Data)
# Sending form data
payload = {
    "username": "admin",
    "password": "1234"
}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.json())
# Sending JSON data
response = requests.post(
    "https://httpbin.org/post",
    json={"name": "Aishwarya", "role": "Developer"}
)


# ✔ Automatically sets:

# Content-Type: application/json

# 7️⃣ PUT & DELETE Requests
requests.put("https://api.example.com/user/1", json={"name": "New Name"})
requests.delete("https://api.example.com/user/1")

# 8️⃣ Sending Headers
headers = {
    "Authorization": "Bearer TOKEN123",
    "User-Agent": "MyApp/1.0"
}

response = requests.get("https://api.example.com", headers=headers)
"""
✔ Used for:

Auth tokens

API keys

Custom metadata
"""

# 9️⃣ Query Parameters
params = {
    "page": 2,
    "limit": 10
}

response = requests.get(
    "https://api.example.com/users",
    params=params
)


# URL becomes:

# https://api.example.com/users?page=2&limit=10

# 🔟 File Upload
files = {
    "file": open("test.txt", "rb")
}

response = requests.post("https://httpbin.org/post", files=files)

# 1️⃣1️⃣ Downloading a File
response = requests.get("https://example.com/file.pdf")

with open("file.pdf", "wb") as f:
    f.write(response.content)

# 1️⃣2️⃣ Timeout Handling ⏱️
response = requests.get("https://example.com", timeout=5)


# ✔ Prevents hanging requests

# 1️⃣3️⃣ Exception Handling (Very Important ⭐)

try:
    response = requests.get("https://example.com", timeout=3)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError:
    print("HTTP error occurred")
except requests.exceptions.RequestException as e:
    print("Error:", e)

# 1️⃣4️⃣ Authentication
# Basic Auth
from requests.auth import HTTPBasicAuth

requests.get(
    "https://api.example.com",
    auth=HTTPBasicAuth("user", "pass")
)

# 1️⃣5️⃣ Session Object (Advanced & Efficient)
session = requests.Session()
session.headers.update({"Authorization": "Bearer TOKEN"})

session.get("https://api.example.com/data")
session.get("https://api.example.com/profile")


# ✔ Reuses connection
# ✔ Faster for multiple requests

# 1️⃣6️⃣ Real-World Example (API Call)

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(user["name"])

"""
1️⃣7️⃣ Common Status Codes
Code	Meaning
200	OK
201	Created
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
500	Server Error
1️⃣8️⃣ requests vs urllib
Feature	requests	urllib
Easy syntax	✅	❌
JSON support	✅	❌
Session support	✅	❌
Readability	⭐⭐⭐⭐⭐	⭐⭐
1️⃣9️⃣ When to Use requests?

✅ Use when:

Calling REST APIs

Web scraping (basic)

Backend integration

Automation scripts

❌ Avoid when:

Async performance needed → use aiohttp

Heavy scraping → use scrapy

2️⃣0️⃣ Interview One-Liner

The requests module is a Python library used to send HTTP requests and interact with web services in a simple and readable way."""