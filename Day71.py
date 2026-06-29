"""cpu_monitor/

│
├── main.py
├── config.json
├── utils.py
├── logs/
│     monitor.log
│
├── reports/
│     report.csv
│
└── README.md"""


"""main.py

Starts the application.

print("CPU Monitor Started")"""


"""config.json

Stores settings.

{
    "cpu_threshold": 80,
    "memory_threshold": 75,
    "interval": 60
}"""


"""utils.py

Contains reusable functions.

Example:

def check_cpu():
    print("Checking CPU")

Later:

from utils import check_cpu

check_cpu()

Instead of copying the same function into five files."""

"""logs/

Stores log files.

logs/

monitor.log

error.log

Never mix logs with source code."""


"""reports/

Stores generated reports.

reports/

daily.csv

weekly.csv"""

"""Why Split Code?

Imagine this:

main.py

1000 lines

Finding one bug becomes difficult.

Instead:

main.py
     ↓
utils.py
     ↓
config.json
     ↓
logs/

Everything has its own place."""


"""Visual Flow
            main.py
               │
      ┌────────┴────────┐
      │                 │
 config.json       utils.py
      │                 │
      └────────┬────────┘
               │
          Business Logic
               │
      ┌────────┴────────┐
      │                 │
   logs/           reports/
"""

