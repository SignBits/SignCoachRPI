import json
import os
from datetime import datetime

from app.info.interface import InfoInterface


class Info:

    name: str
    hardware_version: str
    firmware_version: str
    last_updated: datetime

    file_location: str

    def build(self, file_location: str):
        self.file_location = file_location
        with open(file_location, 'r',) as file:
            info = json.load(file)
            self.name = info['name']
            self.hardware_version = info['hardware_version']
            self.firmware_version = info['firmware_version']
            self.last_updated = float(info['last_updated'])

    def update(self, changes: InfoInterface):
        with open(self.file_location, 'r') as file:
            info = json.load(file)
            for key, val in changes.items():
                info[key] = val
                setattr(self, key, val)

        os.remove(self.file_location)

        with open(self.file_location, 'w') as file:
            json.dump(info, file, indent=4)

        return self

    @property
    def last_updated(self) -> datetime:
        return datetime.utcfromtimestamp(self._last_updated)

    @last_updated.setter
    def last_updated(self, value):
        self._last_updated = value











