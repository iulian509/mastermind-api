from marshmallow import Schema, fields, ValidationError


def validate_value(code):
    if len(code) != 4:
        raise ValidationError("Code length must be 4")


class GameSchema(Schema):
    code = fields.Str(
        required=True,
        validate=validate_value,
    )
    max_tries = fields.Int()
