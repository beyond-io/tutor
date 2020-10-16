from tutor.routes import home, course # noqa
from user_functions import register_and_login
from course_functions import create_test_course


def test_my_courses(client):
    user = register_and_login(client)
    create_test_course(1, "one")
    create_test_course(2, "two")
    # Make sure private courses for user is empty
    response = client.get('/user?id=' + str(user.id), follow_redirects=True)
    assert b"one" not in response.data
    assert b"two" not in response.data
    # add one course to favorites
    client.get('/addfav?course_id=2&user_id=' + str(user.id), follow_redirects=True)
    response = client.get('/user?id=' + str(user.id), follow_redirects=True)
    assert b"one" not in response.data
    assert b"two" in response.data
    # add second course to favorites
    client.get('/addfav?course_id=1&user_id=' + str(user.id), follow_redirects=True)
    response = client.get('/user?id=' + str(user.id), follow_redirects=True)
    assert b"one" in response.data
