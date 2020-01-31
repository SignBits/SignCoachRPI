from marshmallow import fields, Schema


class FingerspellSchema(Schema):
    """Fingerspell schema"""

    characterSequence = fields.String(attribute='sequence')
