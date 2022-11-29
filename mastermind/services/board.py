from difflib import SequenceMatcher

from flask import Response, current_app, abort
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

from mastermind.models.board import Board
from mastermind.common.database import db
from mastermind.schemas.board import BoardSchema


def get_board_status(game_id):
    board_schema = BoardSchema(only=("guess", "black_pegs", "white_pegs"), many=True)
    board = (
        db.session.query(Board)
        .filter(Board.game == game_id)
        .order_by(Board.created_at.desc())
    )
    board_data = board_schema.dump(board)

    return board_data


def check_code_is_guessed(game, json_data):
    if game.code == json_data["guess"]:
        game.solved = True
        board = validate_board_data(json_data, game, 4, 0)
        Board(board["guess"], board["game"], board["black_pegs"], board["white_pegs"])
        db.session.commit()

        return Response(status=200)


def get_black_pegs(game, json_data):
    sequence_match = SequenceMatcher(None, game.code, json_data["guess"])
    longest_match = sequence_match.find_longest_match()
    black_pegs = longest_match.size

    return black_pegs


def get_white_pegs(black_pegs, json_data, game):
    chars_to_check = json_data["guess"][black_pegs:]
    white_pegs = 0
    for c in chars_to_check:
        if c in game.code:
            white_pegs += 1

    return white_pegs


def add_guess_info(json_data, game, black_pegs, white_pegs):
    board = validate_board_data(json_data, game, black_pegs, white_pegs)
    try:
        guess = Board(
            board["guess"], board["game"], board["black_pegs"], board["white_pegs"]
        )
        db.session.add(guess)
        db.session.commit()
    except SQLAlchemyError as err:
        db.session.rollback()
        current_app.logger.error(err)
        abort(400)


def validate_board_data(json_data, game, black_pegs, white_pegs):
    board_schema = BoardSchema()
    try:
        board = board_schema.load(
            {
                "guess": json_data["guess"],
                "game": game.id,
                "black_pegs": white_pegs,
                "white_pegs": black_pegs,
            }
        )
    except ValidationError as err:
        current_app.logger.error(err.messages)
        abort(400)

    return board
