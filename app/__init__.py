from flask import Flask, jsonify
from flask_restplus import Api


def create_app(env='dev'):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__, instance_relative_config=True)
    config = config_by_name[env]
    app.config.from_object(config)
    api = Api(app, title='SignCoach RPI API', version='0.1.0', doc=config.SWAGGER_UI)

    register_routes(api, app)

    @app.route('/health')
    def health():
        return jsonify('healthy')

    return app
