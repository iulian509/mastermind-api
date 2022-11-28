from flask import current_app, abort
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from mastermind.models.game import Game
from mastermind.common.database import db
from mastermind.schemas.game import GameSchema

game_schema = GameSchema()


def create_game(json_data):
    game_data = validate_game_data(json_data)

    try:
        game = Game(game_data["code"], game_data["max_tries"])
        db.session.add(game)
        db.session.commit()
    except SQLAlchemyError as err:
        db.session.rollback()
        current_app.logger.error(err)
        abort(400)

    db.session.refresh(game)

    return {"game_id": game.id}


def validate_game_data(json_data):
    try:
        game_data = game_schema.load(json_data)
    except ValidationError as err:
        current_app.logger.error(err.messages)
        abort(400)

    return game_data


def get_game_info(game_id):
    game = db.session.query(Game).get(game_id)
    return game
