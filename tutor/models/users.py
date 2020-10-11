from .. import db, bcrypt, login_manager
from flask_login import UserMixin


if __name__ == "__main__":
    from ..models.course import Course # noqa


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


# Add favorites tables, to handle many-to-many relationship
favorites = db.Table('favorites',
                     db.Column('user_id', db.Integer,
                               db.ForeignKey('users.id')),
                     db.Column('course_id', db.Integer, db.ForeignKey('course.id')))


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    favorites = db.relationship("Course", secondary=favorites)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def addFavorite(self, course):
        self.favorites.append(course)
        db.session.commit()

    def removeAllFavorites(self):
        self.favorites = []
        db.session.commit()

    def hash_pass(plaintext):
        return bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def __repr__(self):
        return "'id': {0}, 'username': {1}, 'email': {2}".format(self.id, self.username, self.email)
