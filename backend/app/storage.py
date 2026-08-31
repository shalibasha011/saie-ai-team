import json
import os
from typing import Any


DATA_FILE = "saie_data.json"


class Storage:

    def __init__(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as file:
                json.dump({}, file)

    def load(self) -> dict:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    def save(self, data: dict) -> None:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def set(self, key: str, value: Any) -> None:
        data = self.load()
        data[key] = value
        self.save(data)

    def get(self, key: str, default: Any = None) -> Any:
        data = self.load()
        return data.get(key, default)


storage = Storage()