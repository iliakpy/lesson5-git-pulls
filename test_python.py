import math

def test_sorted():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    arr_f = sorted(arr)
    assert arr_f == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_pi():
    assert round(math.pi, 2) == 3.14

def test_pow():
    assert math.pow(2,2) == 4

def test_hypot():
    assert math.hypot(3.0,4.0) == 5.0



assert 2>1