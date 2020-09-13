from .. import db 

class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey(user.id), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(course.id), nullable=False)