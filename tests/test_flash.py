from tutor import app
from tutor.routes import home, course  # noqa


def test_flash_message():
    # check flash message
    c = app.test_client()
    response = c.get('/flash')
    assert b'Test message' in response.data
