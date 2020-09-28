from .. import db
from flask import render_template, redirect, url_for
from .forms import resourceForm
from ..models.course import Resource


def newResource(id):
    form = resourceForm()
    if form.validate_on_submit():
        resource = Resource(title=form.title.data,
                            content=form.content.data, course_id=id)
        db.session.add(resource)
        db.session.commit()
        return redirect(url_for('get_course_info_route', id=id))
    return render_template('resource.html', form=form)
