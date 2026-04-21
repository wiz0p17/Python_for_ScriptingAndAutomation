##“Logged File Analyzer”

'''It should: Scan files

Log:    file processed
        file size
        errors
        Save logs in analyzer.log'''


from pathlib import Path
import logging

path = Path(".")

fileProcessed = 0

logging.basicConfig(filename="analyze.log",level=logging.INFO)

for file in path.rglob("*.py"):
    if file.is_file():
        try:
            logging.info(f"{file.name} - {file.stat().st_size} Bytes")
            fileProcessed += 1

        except Exception as e:
            logging.error(f"An error occoured in {file.name} - {e}")

logging.info(f"Total File processed - {fileProcessed}")
