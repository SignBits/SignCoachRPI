import os
from app import create_app
from app.config import config_by_name
from app.info.model import Info

config = config_by_name[os.getenv('FLASK_ENV', 'prod')]

global_info = Info(config.INFO_FILE_LOC)
app = create_app(config)

if __name__ == '__main__':
    app.run()
