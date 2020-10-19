from tutor import db
from tutor.models.users import Users


def create_test_user(username, email, password):
    user = Users(username=username, email=email, password=Users.hash_pass(password))
    db.session.add(user)
    db.session.commit()
    return search_user_name(username)


def login_test_user(client, email, password):
    login_user = {
        'email': email,
        'password': password,
        'submit': 'Login'
    }
    client.post('/login', data=login_user, follow_redirects=True)


def search_user_name(username):
    return Users.query.filter_by(username=username).first()


def register_and_login(client):
    user = create_test_user(username="test", email="test@email.com", password="123")
    login_test_user(client, "test@email.com", "123")
    return user
