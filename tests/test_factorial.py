from main import factorial


def test_factorial_for_natural_numbers():
     assert factorial(1) == 1
     assert factorial(2) == 2
     assert factorial(3) == 6
     assert factorial(4) == 24


def test_factorial_at_critical_points():
     assert factorial(0) == 1