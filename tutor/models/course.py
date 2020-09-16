from .. import db


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Course('{self.title}')"
