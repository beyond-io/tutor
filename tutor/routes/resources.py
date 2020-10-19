from .. import app
from ..controllers import resources
from flask import request


@app.route("/resource/new", methods=['GET', 'POST'])
def new_resource():
    id = request.args.get('id')
    return resources.newResource(id)


@app.route("/resource/update", methods=['GET', 'POST'])
def update_resource():
    resource_id = request.args.get('resource_id')
    id = request.args.get('id')
    return resources.updateResource(id, resource_id)
