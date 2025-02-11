import json
from notes.notebook import Notebook

def save_notebooks(notebooks, file_path="data/notebooks.json"):
    with open(file_path, "w") as f:
        json.dump([nb.__dict__ for nb in notebooks], f)

def load_notebooks(file_path="data/notebooks.json"):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return [Notebook(**nb) for nb in data]
    except FileNotFoundError:
        return []