#📅 Day 31 – JSON Basics (json module)
"""
From your roadmap :

✅ Parse JSON
✅ Convert Python ↔ JSON
✅ Handle API-style data"""


#Convert Python → JSON (dumps)

"""import json

data = {
    "name":"Vivek",
    "skills": ["python","cloud"]
}

json_data = json.dumps(data)

print(data)
print(json_data)"""



#Convert JSON → Python (loads)

"""import json

json_data = '{"name":"vivek","skills": ["python","cloud"]}'

data = json.loads(json_data)

print(data)
print(data["name"])"""



#Work with JSON Files
"""📌 Write JSON to File"""


"""import json

data = {
    "name": "vivek",
    "skills": ["Python","AWS"]
}

with open("data.json","w") as f:
    json.dump(data,f,indent=4)"""


#Read JSON File

"""import json

with open("data.json","r") as f:
    data = json.load(f)

print(data)"""



##Real AWS-Style Example

"""response = {
    "InstanceId": "i-123456789929",
    "State": "running",
    "Region": "ap-south-1"
}

print(response["InstanceId"])
print(response["Region"])"""


##Save user data to JSON file:

import json

data = {
    "name": "Vivek Negi",
    "instanceID":"i-fkdjfdslkfjdieq",
    "skills": ["Python", "Linux", "AWS"]
}

with open("data.json","w") as f:
    json.dump(data,f,indent=4)
