from flask import render_template, redirect, url_for
from ..models.course import Course
from .forms import AddCourse


def addCourse():
    form = AddCourse()
    if form.validate_on_submit():
        return redirect(url_for('courses_route'))
    return render_template('addcourse.html', form=form)


def showCourses():
    # get courses from data base into a list
    courses = [
        {'id': 1, 'title': 'Course 1'},
        {'id': 2, 'title': 'Course 2'},
        {'id': 3, 'title': 'Course 3'}
    ]
    return render_template('courses.html', courses=courses)


def showCoursePage(id):
    course = Course.query.filter_by(id=id).first()
    name = course.name
    resources = course.resources
    courseId = id
    return render_template('course.html', name=name, resources=resources, id=courseId)
