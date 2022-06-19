from lib.solutions.CHK import checkout_solution



class TestCheckout:
    # def test_checkout_r3(self):
    #     assert checkout_solution.checkout(None) == -1
    #     assert checkout_solution.checkout("") == 0
    #     assert checkout_solution.checkout("A") == 50
    #     assert checkout_solution.checkout("B") == 30
    #     assert checkout_solution.checkout("C") == 20
    #     assert checkout_solution.checkout("D") == 15
    #     assert checkout_solution.checkout("a") == -1
    #     assert checkout_solution.checkout("-") == -1
    #     assert checkout_solution.checkout("ABCa") == -1
    #     assert checkout_solution.checkout("AxA") == -1
    #     assert checkout_solution.checkout("ABCD") == 115
    #     assert checkout_solution.checkout("A") == 50
    #     assert checkout_solution.checkout("AA") == 100
    #     assert checkout_solution.checkout("AAA") == 130
    #     assert checkout_solution.checkout("AAAA") == 180
    #     assert checkout_solution.checkout("AAAAA") == 200
    #     assert checkout_solution.checkout("AAAAAA") == 250
    #     assert checkout_solution.checkout("B") == 30
    #     assert checkout_solution.checkout("BB") == 45
    #     assert checkout_solution.checkout("BBB") == 75
    #     assert checkout_solution.checkout("BBBB") == 90
    #     assert checkout_solution.checkout("ABCDABCD") == 215
    #     assert checkout_solution.checkout("BABDDCAC") == 215
    #     assert checkout_solution.checkout("AAABB") == 175
    #     assert checkout_solution.checkout("ABCDCBAABCABBAAA") == 495
    #     assert checkout_solution.checkout("EE") == 80
    #     assert checkout_solution.checkout("EEB") == 80
    #     assert checkout_solution.checkout("EEBB") == 110
    #     assert checkout_solution.checkout("EEBBB") == 125
    #     assert checkout_solution.checkout("EEEEBBBB") == 205
    #     assert checkout_solution.checkout("EEEEEEBBBB") == 270
    #     assert checkout_solution.checkout("EEEEBBBBAAAAAA") == 455
    #     assert checkout_solution.checkout("FF") == 20
    #     assert checkout_solution.checkout("FFF") == 20
    #     assert checkout_solution.checkout("FFFF") == 30
    #
    # def test_checkout_r4(self):
    #     assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965
    #     assert checkout_solution.checkout("HHHHH") == 45
    #     assert checkout_solution.checkout("HHHHHHHHH") == 85
    #     assert checkout_solution.checkout("HHHHHHHHHH") == 80
    #     assert checkout_solution.checkout("K") == 80
    #     assert checkout_solution.checkout("KK") == 150
    #     assert checkout_solution.checkout("KKK") == 230
    #     assert checkout_solution.checkout("KKKK") == 300
    #     assert checkout_solution.checkout("NNN") == 120
    #     assert checkout_solution.checkout("NNNM") == 120
    #     assert checkout_solution.checkout("NNNMM") == 135
    #     assert checkout_solution.checkout("PPPP") == 200
    #     assert checkout_solution.checkout("PPPPP") == 200
    #     assert checkout_solution.checkout("PPPPPP") == 250
    #     assert checkout_solution.checkout("QQQ") == 80
    #     assert checkout_solution.checkout("QQQQ") == 110
    #     assert checkout_solution.checkout("QQQQQQ") == 160
    #     assert checkout_solution.checkout("QQQQQQQ") == 190
    #     assert checkout_solution.checkout("RRR") == 150
    #     assert checkout_solution.checkout("RRRQ") == 150
    #     assert checkout_solution.checkout("RRRQQ") == 180
    #     assert checkout_solution.checkout("UUU") == 120
    #     assert checkout_solution.checkout("UUUU") == 120
    #     assert checkout_solution.checkout("UUUUU") == 160
    #     assert checkout_solution.checkout("VV") == 90
    #     assert checkout_solution.checkout("VVV") == 130
    #     assert checkout_solution.checkout("VVVV") == 180

    def test_checkout_r5(self):
        assert checkout_solution.checkout("STXSTX") == 45








