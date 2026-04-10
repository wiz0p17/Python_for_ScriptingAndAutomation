'''Go to a folder
Create a subfolder called logs
Create a file inside it'''

from pathlib import Path

path = Path("/Users/vivek/Downloads")

file = path / "Logs/test.txt"
file.mkdir()
file.touch()

