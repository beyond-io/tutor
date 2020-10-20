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


@app.route("/newfavorites", methods=['GET', 'POST'])
def newFavorites_route():
    return course.addCourseToFavorites()

 
@app.route("/addcourse", methods=['GET', 'POST'])
def addCourse_route():
    return course.addCourseToTutor()
