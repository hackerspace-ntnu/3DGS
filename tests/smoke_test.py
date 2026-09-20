import numpy as np


def test_numpy_available():
    x = np.array([1.0, 2.0, 3.0])
    assert np.linalg.norm(x) > 0.0