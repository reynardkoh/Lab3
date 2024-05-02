import Lab2.bmi as BMI

def test_bmi_normal_weight():
    result = BMI.weight_class(18.6)
    assert (result == 0)
def test_bmi_over_weight():
    result = BMI.weight_class(26.0)
    assert (result == 1)
def test_bmi_under_weight():
    result = BMI.weight_class(16.5)
    assert (result == -1)

