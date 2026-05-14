#“Simple CRUD Tool”
"""
It should:

GET one post
CREATE one post
UPDATE it
DELETE it"""


import requests

#get
response = requests.get("https://jsonplaceholder.typicode.com/posts/1",timeout=10)

data = response.json()
print("id :",data['id'])

payload = {
    "title":"Who is modi",
    "body":"Modi is PM of India"
    }

#create
updated = requests.post(f"https://jsonplaceholder.typicode.com/posts/",json=payload)

data2 = updated.json()

print(data2)

#update
updated = requests.put(f"https://jsonplaceholder.typicode.com/posts/{data2["id"]}",json={"title":"Modi Modi Modi","body":"Modi is Modi"})

print(updated.status_code)

#delete

deleted = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{data2["id"]}",timeout=10)

print("Deleted Status:",deleted.status_code)


