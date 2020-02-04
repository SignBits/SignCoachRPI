from flask import Flask, jsonify
from flask_restplus import Api

from app.config import config_by_name

from app.info.model import Info


info = Info()


def create_app(config_mode):
    from app.routes import register_routes

    app = Flask(__name__, instance_relative_config=True)

    config_obj = config_by_name[config_mode]

    app.config.from_object(config_obj)

    api = Api(app, title='SignCoach RPI API', version='0.1.0', doc=config_obj.SWAGGER_URI)

    register_routes(api, app)
    info.build(config_obj.INFO_FILE_LOC)

    @app.route('/health')
    def health():
        return jsonify('healthy')

    return app
