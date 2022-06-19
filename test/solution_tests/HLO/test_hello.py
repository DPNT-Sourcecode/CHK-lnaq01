from lib.solutions.HLO import hello_solution


class TestSum:
    def test_sum_int(self):
        assert hello_solution.hello("ignore") == "Hello There"

