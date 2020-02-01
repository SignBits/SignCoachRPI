from marshmallow import fields, Schema


class InfoSchema(Schema):
    """Info schema"""

    deviceName = fields.String(attribute='name')
    hardwareVersion = fields.String(attribute='hardware_version', dump_only=True)
    firmwareVersion = fields.String(attribute='firmware_version', dump_only=True)
    lastUpdated = fields.DateTime(attribute='last_updated', dump_only=True)
