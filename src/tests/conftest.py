import pytest
from server import build_app


@pytest.fixture()
def app():
    flask_app = build_app()
    flask_app.config.update(
        {
            "TESTING": True,
        }
    )
    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
