#“EC2 JSON Parser”
"""
It should:

Store fake EC2 response
Print:
Instance ID
State
Region"""

data = {
    "Instances": [
        {
            "InstanceId": "i-123456",
            "State": {
                "Name": "running"
            },
            "Region": "ap-south-1"
        }
    ]
}

instance = data["Instances"][0]

print("Instance ID: ",instance["InstanceId"])
print("State: ",instance["State"]["Name"])
print("Region: ",instance["Region"])