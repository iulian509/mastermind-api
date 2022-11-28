def test_status(test_client):
    resp = test_client.get("/status")
    assert resp.status_code == 200
