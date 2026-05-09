#📅 Day 32 – Nested JSON & API-Style Data

"""From your roadmap :

✅ Work with nested JSON
✅ Parse API responses
✅ Extract useful data from complex structures"""

"""data = {
    "user": {
        "name": "Vivek",
        "skills": ["Python", "AWS"]
    }
}


print(data["user"]["name"])
print(data["user"]["skills"][0])"""


"""response = {
    "Instances": [
        {
            "id": "i-123",
            "state": "running"
        },
        {
            "id": "i-456",
            "state": "stopped"
        }
    ]
}

print(response["Instances"][1]["state"])

for instances in response["Instances"]:
    print(instances["id"], instances["state"])"""


"""data = {
    "Reservations": [
        {
            "Instances": [
                {
                    "InstanceId": "i-12345",
                    "State": {
                        "Name": "running"
                    }
                }
            ]
        }
    ]
}


instance = data["Reservations"][0]["Instances"][0]

print(instance)
print(instance["InstanceId"],instance["State"]["Name"])

state = instance.get("State",{}).get("Name")

print(state)
"""

data = {
    "employee": {
        "name": "Vivek",
        "department": {
            "name": "Cloud",
            "location": "India"
        }
    }
}

print(data["employee"]["name"])
print(data["employee"]["department"])






