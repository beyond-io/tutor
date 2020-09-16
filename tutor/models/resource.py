from .. import db
from datetime import datetime


class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __init__(self, title, content, link, course_id):
        self.title = title
        self.date_posted = datetime.today()
        self.content = content
        self.link = link
        self.course_id = course_id

    def __repr__(self):
        return f"Resource('{self.title}', '{self.date_posted}')"
