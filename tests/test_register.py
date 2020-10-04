from tutor import app, db, bcrypt
from tutor.routes import home, course # noqa
from tutor.models.users import Users


def test_register_user():
    with app.test_client() as c:
        # Test register user
        assert Users.query.all() == []
        user = {
            'username': 'test',
            'email': 'test@email.com',
            'password': '123',
            'confirm_password': '123',
            'submit': 'Sign Up'
        }
        # Register new user
        c.post('/register', data=user, follow_redirects=True)
        test_user = Users.query.first()
        # Test new user
        assert test_user.username == 'test'
        assert test_user.email == 'test@email.com'
        # Test password hash
        assert bcrypt.check_password_hash(test_user.password, '123')
        # Test trying to register an already registered username and email
        response = c.post('/register', data=user, follow_redirects=True)
        assert b'Username already registered' and b'Email already registered' in response.data
    # Delete new user
    Users.query.delete()
    db.session.commit()
