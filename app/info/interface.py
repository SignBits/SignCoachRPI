from datetime import datetime
from mypy_extensions import TypedDict


class InfoInterface(TypedDict):

    name: str
    hardware_version: str
    firmware_version: str
    last_updated: datetime
