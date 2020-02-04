import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = 'base'
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    INFO_FILE_LOC = './info.json'
    SWAGGER_URI = '/'


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = 'dev'
    SECRET_KEY = os.getenv("DEV_SECRET_KEY", "")
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    CONFIG_NAME = 'test'
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "")
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    CONFIG_NAME = 'prod'
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "")
    DEBUG = False
    TESTING = False
    SWAGGER_URI = None


EXPORT_CONFIGS: List[Type[BaseConfig]] = [DevelopmentConfig, TestingConfig, ProductionConfig]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
