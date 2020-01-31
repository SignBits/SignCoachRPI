from flask import request

from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource

from app.fingerspell.schema import FingerspellSchema
from app.fingerspell.service import FingerspellService

api = Namespace('Fingerspell', description='SignCoach fingerspell endpoint')


@api.route('/')
class FingerspellResource(Resource):
    """Operations"""

    @accepts(schema=FingerspellSchema, api=api)
    @responds(schema=FingerspellSchema)
    def post(self) -> None:
        """Submit a sequence for the robot to fingerspell."""
        FingerspellService.submit_sequence(request.parsed_obj)
