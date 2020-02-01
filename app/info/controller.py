from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource

from app.info.model import Info
from app.info.schema import InfoSchema
from app.info.interface import InfoInterface
from app.info.service import InfoService

api = Namespace('Info', description='SignCoach info endpoint')


@api.route('/')
class InfoResource(Resource):
    """Info"""

    @responds(schema=InfoSchema, api=api)
    def get(self) -> Info:
        """Get current Coach info."""
        return InfoService.get()

    @accepts(schema=InfoSchema, api=api)
    @responds(schema=InfoSchema, api=api)
    def put(self) -> Info:
        """Update current config"""

        changes: InfoInterface = request.parsed_obj
        return InfoService.update(changes)
