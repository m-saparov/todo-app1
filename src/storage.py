import json
import os

FILE_NAME = "database.json"


def init_storage():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f, indent=4)

def read_file():
    init_storage()
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_file(tasks: list):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
