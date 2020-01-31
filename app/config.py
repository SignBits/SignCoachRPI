import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = 'base'
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = 'dev'
    SECRET_KEY = os.getenv("DEV_SECRET_KEY", "")
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class TestingConfig(BaseConfig):
    CONFIG_NAME = 'test'
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "")
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


class ProductionConfig(BaseConfig):
    CONFIG_NAME = 'prod'
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


EXPORT_CONFIGS: List[BaseConfig] = [
    DevelopmentConfig, TestingConfig, ProductionConfig]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
