import os

print("Script start ho gaya...")

folders = ["data", "notebook", "src", "artifacts"]

files = [
    "src/data_ingestion.py",
    "src/data_processing.py",
    "src/model_trainer.py",
    "src/predict.py",
    "notebook/experiment.ipynb",
    "app.py",
    "requirements.txt",
    "README.md"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print("Folder created:", folder)

for file in files:
    with open(file, "w") as f:
        pass
    print("File created:", file)

print("Project structure created successfully!")