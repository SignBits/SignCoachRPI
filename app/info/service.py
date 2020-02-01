from app.info.interface import InfoInterface
from app.info.model import Info
from run import global_info


class InfoService:

    @staticmethod
    def get() -> Info:
        return global_info

    @staticmethod
    def update(info_change_updates: InfoInterface):
        global_info.update(info_change_updates)
        return global_info

