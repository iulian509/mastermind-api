from flask import Blueprint, request, abort, jsonify

from mastermind.services.game import create_game

game_bp = Blueprint("game", __name__)


@game_bp.route("/game", methods=["POST"])
def game():
    json_data = request.get_json()

    if request.content_type != "application/json" or not json_data:
        abort(400)

    resp = create_game(json_data)

    return jsonify(resp)
