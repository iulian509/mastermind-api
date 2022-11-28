import pytest
from main import create_app


@pytest.fixture(scope="class")
def test_client():
    flask_app = create_app()

    testing_client = flask_app.test_client()

    with flask_app.app_context():
        yield testing_client
