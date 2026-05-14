##📅 Day 37 – GET, POST, PUT & DELETE
"""
From your roadmap :

✅ Understand CRUD
✅ Use PUT & DELETE
✅ Build complete API workflows"""


#🌐 2. GET Request (Read Data)
"""
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.json())"""


#🔥 3. POST Request (Create Data)
"""
import requests

payload = {
    "title" : "Python Automation",
    "body" : "Python Automation for beginners"
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",json = payload,timeout=5)

print(response.json())"""



#✏️ 4. PUT Request (Update Data)
"""
import requests

payload = {
    "id": 1,
    "title": "Python Scripting",
    "body" : "Python Automation for beginners"
}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1",json=payload,timeout=5)

print(response.json())"""


#❌ 5. DELETE Request
"""
import requests

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1",timeout=5)

print(response.status_code)"""


#⚠️ 6. Status Codes (VERY IMPORTANT)
"""
Code Meaning
200	Success
201	Created
400	Bad request
401	Unauthorized
404	Not found
500	Server error"""


#🛡️ 7. Production Safety Pattern
"""
try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

except requests.exceptions.RequestException as e:
    print("API Error:", e)"""


###🔥 8. Real Workflow Example

#👉 Create → Update → Delete
"""
import requests

data = {
    "id":58,
    "title": "devops"
}
#create
create = requests.post("https://jsonplaceholder.typicode.com/posts",json=data,timeout=10)

post = create.json()

print("Creation id :",post)
id = post["id"]
print(id)

#update
updated = requests.put(f"https://jsonplaceholder.typicode.com/posts/{id}",json={"title":"Updated Devops"})

print(updated.status_code)

#delete
deleted = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{id}",timeout=5)

print("Deleted Status: ",deleted.status_code)"""


##🧪 9. Mini Practice (DO THIS)

#👉 Update a fake post:

import requests

response = requests.put("https://jsonplaceholder.typicode.com/posts/1",json ={"title":"new title"},timeout=15)

print(response.json())




