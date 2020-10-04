from tutor import app, db
from tutor.routes import home, course # noqa
from tutor.models.users import Users


def test_login():
    with app.test_client() as c:
        # Test login without register
        login_user = {
            'email': 'test@email.com',
            'password': '123',
            'submit': 'Login'
        }
        response = c.post('/login', data=login_user, follow_redirects=True)
        assert b'Login unsuccessful' in response.data
        # Create test user
        register_user = {
            'username': 'test',
            'email': 'test@email.com',
            'password': '123',
            'confirm_password': '123',
            'submit': 'Sign Up'
        }
        c.post('/register', data=register_user, follow_redirects=True)
        # Test user login
        response = c.post('/login', data=login_user, follow_redirects=True)
        assert b'Welcome' in response.data
        # Test login after user already logged in
        response = c.post('/login', data=login_user, follow_redirects=True)
        assert b'You are already logged in' in response.data
    Users.query.delete()
    db.session.commit()
