from tutor.models.course import Course
from user_functions import search_user_name, create_test_user


def test_fav(client):
    # create new user
    create_test_user(
        username='pypy', email='email@email.com', password='pass')

    # check that user exists and has no favorites
    user = search_user_name('pypy')
    assert [] == user.favorites

    # create new course and add it to the user's favorites
    c = Course(name="python course")
    user.addFavorite(c)

    # check the course added to user favorites
    same_user = search_user_name('pypy')
    assert c == same_user.favorites[0]
