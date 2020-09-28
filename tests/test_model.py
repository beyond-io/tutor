from tutor.models.model import Model


def test_add_new_model():
    # check Model properties
    model = Model(name='tester')
    assert model.name == 'tester'
    # check Model save() method
    model.save()
    testModel = Model.getFirstByName('tester')
    assert testModel.name == 'tester'
    # check Model delete() method
    model.delete()
    assert Model.getAllByName('tester') == []
