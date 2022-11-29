import json


def test_create_game(test_client):
    data = {"code": "RGBY", "max_tries": 10}
    resp = test_client.post(
        "/game", data=json.dumps(data), headers={"Content-type": "application/json"}
    )
    assert resp.status_code == 200


def test_create_game_incorrect_content_type(test_client):
    data = {"code": "RGBY", "max_tries": 10}
    resp = test_client.post(
        "/game",
        data=json.dumps(data),
        headers={"Content-type": "application/x-www-form-urlencoded"},
    )
    assert resp.status_code == 400


def test_create_game_no_payload(test_client):
    data = {}
    resp = test_client.post(
        "/game",
        data=json.dumps(data),
        headers={"Content-type": "application/json"},
    )
    assert resp.status_code == 400


def test_create_game_incorrect_payload(test_client):
    data = {"code": "RGBY", "tries": 10}
    resp = test_client.post(
        "/game",
        data=json.dumps(data),
        headers={"Content-type": "application/json"},
    )
    assert resp.status_code == 400


def test_create_game_incorrect_length(test_client):
    data = {"code": "RGBYXX", "tries": 10}
    resp = test_client.post(
        "/game",
        data=json.dumps(data),
        headers={"Content-type": "application/json"},
    )
    assert resp.status_code == 400
