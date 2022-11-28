from marshmallow import Schema, fields, ValidationError


def validate_value(guess):
    if len(guess) != 4:
        raise ValidationError("Guess length must be 4")


class BoardSchema(Schema):
    guess = fields.Str(
        required=True,
        validate=validate_value,
    )
    game = fields.Int()
    black_pegs = fields.Int()
    white_pegs = fields.Int()
