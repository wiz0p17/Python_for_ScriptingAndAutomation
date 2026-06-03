#Safe Report Generator
"""
Requirements:

Create folder: reports

Don't fail if folder exists.

Create:report.txt

only if it doesn't exist.

Print: Report Ready"""


from pathlib import Path

folder = Path("reports")

folder.mkdir(exist_ok=True)

print("Folder is ready!")

reportFile = folder / "report.txt"

if not reportFile.exists():
    reportFile.write_text(
        "Cloud Monitoring Report"
    )

print("Report Ready!")