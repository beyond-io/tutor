from flask import jsonify
from ..models import model


def getAllModels():
    models = model.Model.query.all()
    return jsonify([e.serialize() for e in models])


def createNewModel(modelName):
    modeling = model.Model(name=modelName)
    modeling.save()
    return jsonify({'id': modeling.id, 'status': 200})
