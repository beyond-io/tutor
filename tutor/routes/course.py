from .. import app
from ..controllers import course
from flask import request


@app.route('/course')
def get_course_info_route():
    id = request.args.get('id')
    return course.showCoursePage(id)


@app.route("/courses", methods=['GET', 'POST'])
def courses_route():
    return course.showCourses()


@app.route("/addcourse", methods=['GET', 'POST'])
def addCourse_route():
    return course.addCourse()


@app.route("/addfav", methods=['GET', 'POST'])
def fav_route():
    course_id = request.args.get('course_id')
    user_id = request.args.get('user_id')
    return course.addCourseToFav(course_id, user_id)
