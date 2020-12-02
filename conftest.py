import os
import tempfile
import pytest
from serverTeSt import app as flask_app

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = flask_app
    app.config['TESTING'] = True
    app.config['DATABASE'] = db_path

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()