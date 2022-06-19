from lib.solutions.SUM import sum_solution


class TestSum:
    def test_sum_int(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_zero(self):
        assert sum_solution.compute(0, 0) == 0

    def test_sum_float(self):
        assert sum_solution.compute(1.3, 2.7) == 4.0
        assert sum_solution.compute(1.3555, 2.7777) != 4.1332 # Shows floating point error

    def test_sum_string(self):
        assert sum_solution.compute("Hello", " World") == "Hello World"
        assert sum_solution.compute("Hello", "") == "Hello"
        assert sum_solution.compute("", " World") == " World"
        assert sum_solution.compute("", "") == ""

    def test_sum_none(self):
        assert sum_solution.compute(None, None) is None
        assert sum_solution.compute(None, 1) is None
        assert sum_solution.compute(1, None) is None




