from tutor import db
from tutor.models.course import Course, Resource
import pandas as pd


data = pd.read_csv('data.csv')
courses = pd.unique(data['Name'])  # get all courses names without duplicates

for course_name in courses:
    new_course = Course(name=course_name)
    db.session.add(new_course)
    course_id = Course.query.filter_by(name=course_name).first().id  # for making new resources
    resources = data[data['Name'] == course_name]  # all rows of Course_Name in the file
    # add all resources related to given course
    for resource in resources.iterrows():
        title = resource[1]['Title']
        content = resource[1]['Content']
        link = resource[1]['Link']
        # make new resourse, attach it to desired course and add it into db
        new_resource = Resource(title=title, content=content, link=link, course_id=course_id)
        db.session.add(new_resource)
db.session.commit()
