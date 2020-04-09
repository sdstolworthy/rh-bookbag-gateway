from bookbag.app import create_app
from bookbag.settings import DevConfig

CONFIG = DevConfig

app = create_app(DevConfig)
