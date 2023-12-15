from Model import IrisModel

def test_predict():
    """
    Test for IrisModel.predict_species
    """

    model = IrisModel()
    prediction_results = model.predict_species(1.0, 2.0, 3.0, 4.0)

    assert len(prediction_results) == 2
    assert 0 <= prediction_results[1] <= 1