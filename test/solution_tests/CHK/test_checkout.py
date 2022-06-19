from lib.solutions.CHK import checkout_solution


class TestSum:
    def test_sum_int(self):
        assert checkout_solution.checkout(None) == -1
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("-") == -1
        assert checkout_solution.checkout("ABCa") == -1  # We are unsure if this is a valid sku string or not, we'll
        # find out after we've deployed it again
        assert checkout_solution.checkout("AxA") == -1
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAA") == 230
        assert checkout_solution.checkout("AAAAAA") == 260
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBB") == 75
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("ABCDABCD") == 215
        assert checkout_solution.checkout("BABDDCAC") == 215
        assert checkout_solution.checkout("AAABB") == 175
        assert checkout_solution.checkout("ABCDCBAABCABBAAA") == 505
