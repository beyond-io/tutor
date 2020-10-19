from .. import db
from flask import render_template, redirect, url_for, request
from ..models.course import Resource
from .forms.resource_form import ResourceForm


def newResource(id):
    form = ResourceForm()
    if form.validate_on_submit():
        resource = Resource(title=form.title.data,
                            content=form.content.data, link=form.link.data, course_id=id)
        db.session.add(resource)
        db.session.commit()
        return redirect(url_for('get_course_info_route', id=id))
    return render_template('resource.html', form=form)

def updateResource(id, resource_id):
    resource=Resource.query.filter_by(id=resource_id).first()
    form = ResourceForm()
    if form.validate_on_submit():
        resource.title=form.title.data
        resource.content=form.content.data
        resource.link=form.link.data
        db.session.commit()
        return redirect(url_for('get_course_info_route', id=id))
    elif request.method == 'GET':
        form.title.data=resource.title
        form.content.data=resource.content
        form.link.data=resource.link

    return render_template('resource.html', form=form)