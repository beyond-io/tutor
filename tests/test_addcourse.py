from tutor import app, db
from tutor.routes import home, course # noqa
from tutor.models.course import Course


def test_addcourse():
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TESTING'] = True
    with app.test_client() as c:
        assert Course.query.all() == []
        course1 = {'name': 'Open Source'}
        c.post('/addcourse', data=course1, follow_redirects=True)
        test_course = Course.query.first()
        assert test_course.name == 'Open Source'
    Course.query.delete()
    db.session.commit()
