import unittest

from cancer_prediction_mm2921 import cancer_model


class TestCancerModel(unnitest.TestCase):
    def test_diagnosis_to_target():
        model = CancerModel()
        diagnosis = "Malignant"
        target = model.diagnosis_to_target(diagnosis)
        self.assertEqual(target, 0)

        diagnosis = "Benign"
        target = model.diagnosis_to_target(diagnosis)
        self.assertEqual(target, 1)

    def test_target_to_diagnosis(self):
        model = CancerModel()
        target = 0
        diagnosis = model.target_to_diagnosis(target)
        self.assertEqual(diagnosis, "Malignant")

        target = 1
        diagnosis = model.target_to_diagnosis(target)
        self.assertEqual(diagnosis, "Benign")


if __name__ == "__main__":
    unittest.main()
