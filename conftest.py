import os
import pytest
from main import create_app


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    flask_app.config.from_object("settings.TestingConfig")
    testing_client = flask_app.test_client()

    with flask_app.app_context():
        yield testing_client

    os.remove("instance/mastermind-test.db")
