from flask import Flask, jsonify
from flask_restplus import Api


def create_app(config_object):
    from app.routes import register_routes

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)
    api = Api(app, title='SignCoach RPI API', version='0.1.0', doc=config_object.SWAGGER_URI)

    register_routes(api, app)

    @app.route('/health')
    def health():
        return jsonify('healthy')

    return app
