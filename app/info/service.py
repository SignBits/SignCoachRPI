from app.info.interface import InfoInterface
from app.info.model import Info

from app import info


class InfoService:

    @staticmethod
    def get() -> Info:
        return info

    @staticmethod
    def update(info_change_updates: InfoInterface):
        info.update(info_change_updates)
        return info

