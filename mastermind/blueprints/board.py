from flask import Blueprint, Response, request, abort, jsonify

from mastermind.services.board import (
    get_board_status,
    check_code_is_guessed,
    get_black_pegs,
    get_white_pegs,
    add_guess_info,
)
from mastermind.services.game import get_game_info


board_bp = Blueprint("board", __name__)


@board_bp.route("/board/<game_id>", methods=["GET"])
def get_game_state(game_id):
    board = get_board_status(game_id)

    return jsonify(board)


@board_bp.route("/board/<game_id>", methods=["POST"])
def add_guess(game_id):
    json_data = request.get_json()

    if request.content_type != "application/json" or not json_data:
        abort(400)

    game = get_game_info(game_id)
    board = get_board_status(game_id)
    if game.resolved or game.finished or len(board) >= game.max_tries:
        abort(400)

    check_code_is_guessed(game, json_data)
    black_pegs = get_black_pegs(game, json_data)
    white_pegs = get_white_pegs(black_pegs, json_data, game)
    add_guess_info(json_data, game, black_pegs, white_pegs)

    return Response(status=200)
