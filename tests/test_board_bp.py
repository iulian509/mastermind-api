import json
import pytest

from mastermind.services.game import create_game


@pytest.fixture
def game_fixture():
    data = {"code": "RGBY", "max_tries": 10}
    create_game(data)


def test_get_board(test_client, game_fixture):
    game_id = 1
    resp = test_client.get(f"/board/{game_id}")
    assert resp.status_code == 200


def test_get_board_dont_exist(test_client):
    game_id = 2
    resp = test_client.get(f"/board/{game_id}")
    assert resp.status_code == 404


def test_add_guess_incorrect_length(test_client, game_fixture):
    game_id = 1
    data = {"guess": "RGBYXX"}
    resp = test_client.post(
        f"/board/{game_id}",
        data=json.dumps(data),
        headers={"Content-type": "application/json"},
    )
    assert resp.status_code == 400


def test_add_incorrect_guess(test_client, game_fixture):
    game_id = 1
    data = {"guess": "RGXX"}
    resp = test_client.post(
        f"/board/{game_id}",
        data=json.dumps(data),
        headers={"Content-type": "application/json"},
    )
    assert resp.status_code == 200


def test_add_guess(test_client, game_fixture):
    game_id = 1
    data = {"guess": "RGBY"}
    resp = test_client.post(
        f"/board/{game_id}",
        data=json.dumps(data),
        headers={"Content-type": "application/json"},
    )
    assert resp.status_code == 200


def test_add_guess_incorrect_content_type(test_client, game_fixture):
    game_id = 1
    data = {"guess": "RGBY"}
    resp = test_client.post(
        f"/board/{game_id}",
        data=json.dumps(data),
        headers={"Content-type": "application/x-www-form-urlencoded"},
    )
    assert resp.status_code == 400


def test_add_guess_empty_payload(test_client, game_fixture):
    game_id = 1
    data = {}
    resp = test_client.post(
        f"/board/{game_id}",
        data=json.dumps(data),
        headers={"Content-type": "application/json"},
    )
    assert resp.status_code == 400


def test_add_guess_already_solved(test_client, game_fixture):
    game_id = 1
    data = {"guess": "RGBY"}
    resp = test_client.post(
        f"/board/{game_id}",
        data=json.dumps(data),
        headers={"Content-type": "application/json"},
    )
    assert resp.status_code == 400
