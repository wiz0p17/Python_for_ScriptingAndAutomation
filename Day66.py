#JSON Configuration Files (The DevOps Way)

"""import json

with open("config.json") as file:
    config = json.load(file)

print(config)"""

"""
import json

config = {
    "region": "ap-south-1",
    "cpu_threshold": 80
}


with open("config.json","w") as file:
    json.dump(config,file,indent=4)"""


import json

with open("config.json","r") as file:
    config = json.load(file)

    print(config["cpu_threshold"])

cpu = 88

if cpu > config["cpu_threshold"]:
    print("send alert")

