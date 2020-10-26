from tutor.routes import home, course, resources # noqa
from course_functions import create_test_course, search_resource_title, create_test_resource
from tutor.models.course import Resource


def test_resource_create(client):
    create_test_course(3000, "test_course")
    resource = {
        'title': 'resource_name',
        'content': 'content',
        'link': 'https://www.google.com',
        'submit': 'Post'
    }
    client.post('/resource/new?id=3000', data=resource, follow_redirects=True)
    test_resource = search_resource_title("resource_name")
    assert test_resource.title == 'resource_name'
    assert test_resource.content == 'content'
    assert test_resource.link == 'https://www.google.com'


def test_resource_edit(client):
    create_test_course(3000, "test_course")
    create_test_resource(200, "resource_name", "content", "https://www.google.com", 3000)
    edited_data = {
        'title': 'edited resource_name',
        'content': 'edited content',
        'link': 'https://www.yahoo.com',
        'submit': 'Post'
    }
    client.post('/resource/update?id=3000&resource_id=200', data=edited_data, follow_redirects=True)
    test_resource = Resource.query.filter_by(id=200).first()
    assert test_resource.title == 'edited resource_name'
    assert test_resource.content == 'edited content'
    assert test_resource.link == 'https://www.yahoo.com'
