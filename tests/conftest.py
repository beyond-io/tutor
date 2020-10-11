import pytest
from tutor import app, db
from tutor.models.course import Resource, Course
from tutor.models.users import Users


@pytest.fixture
def client():
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TESTING'] = True
    return app.test_client()


@pytest.fixture(autouse=True)
def cleanup():
    yield None
    for user in Users.query.all():
        user.removeAllFavorites()
    Resource.query.delete()
    Course.query.delete()
    Users.query.delete()
    db.session.commit()
