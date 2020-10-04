from tutor import app
from tutor.routes import home, course, resources # noqa
from tutor import db
from tutor.models.course import Resource, Course


def test_resource_create():
    with app.test_client() as c:
        assert Resource.query.all() == []
        course_1 = Course(id=3000, name='course_name')
        db.session.add(course_1)
        db.session.commit()
        resource = {
            'title': 'resource_name',
            'content': 'content',
            'link': 'https://www.google.com',
            'submit': 'Post'
        }
        c.post('/resource/new?id=3000', data=resource, follow_redirects=True)
        test_resource = Resource.query.filter_by(title='resource_name').first()
        assert test_resource.title == 'resource_name'
        assert test_resource.content == 'content'
        assert test_resource.link == 'https://www.google.com'
    db.session.delete(test_resource)
    db.session.delete(course_1)
    db.session.commit()
