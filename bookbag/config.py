import os


class BaseConfig(object):
    DEBUG = False
    FAKED = False
    OC_SERVICE_TOKEN = ''
    OC_API_BASE_URL = ''


class FakedConfig(object):
    FAKED = True
    DEBUG = True


class ProductionConfig(object):
    OC_SERVICE_TOKEN = os.environ.get('OC_SERVICE_TOKEN')
    OC_API_BASE_URL = os.environ.get('OC_API_BASE_URL')
