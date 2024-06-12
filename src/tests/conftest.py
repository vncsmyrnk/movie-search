import pytest
from server import build_app
from search.file import read_index, read_vocab


@pytest.fixture()
def vocab():
    return read_vocab()


@pytest.fixture()
def index():
    return read_index()


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
