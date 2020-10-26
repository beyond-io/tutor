from tutor import db
from tutor.models.course import Resource, Course


def create_test_course(course_id, name):
    course = Course(id=course_id, name=name)
    db.session.add(course)
    db.session.commit()


def create_test_resource(id, title, content, link, course_id):
    resource = Resource(id=id, title=title, content=content, link=link, course_id=course_id)
    db.session.add(resource)
    db.session.commit()


def search_course_name(name):
    return Course.query.filter_by(name=name).first()


def search_resource_title(title):
    return Resource.query.filter_by(title=title).first()
