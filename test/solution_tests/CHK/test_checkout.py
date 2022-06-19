from lib.solutions.CHK import checkout_solution


class TestSum:
    def test_sum_int(self):
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("A") == 50


