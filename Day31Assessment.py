#“System Info JSON Exporter”

"""It should:

Create dictionary with:
username
OS name
favorite skill
Save into system_info.json"""

import json

data = {
    "username":"inspireUAT",
    "OSname":"Windows",
    "Skills":"Linux"
}

with open("system_info.json","w") as f:
    json.dump(data,f,indent=4)