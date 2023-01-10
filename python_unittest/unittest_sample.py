import unittest


class Calculator:
    def mod(self, dividend, divisor):
        remainder = dividend % divisor
        quotient = (dividend - remainder) / divisor
        return quotient, remainder


class CalculatorTest(unittest.TestCase):

    def test_mod_with_remainder(self):
        cal = Calculator()
        self.assertEqual(cal.mod(5, 3), (1, 2))

    def test_mod_without_remainder(self):
        cal = Calculator()
        self.assertEqual(cal.mod(8, 4), (1, 0))

    def test_mod_divide_by_zero(self):
        cal = Calculator()
        assertRaises(ZeroDivisionError, cal.mod, 7, 1)


if __name__ == '__main__':
    unittest.main()

    """
    參考至: https://imsardine.wordpress.com/tech/unit-testing-in-python/
    1. E.F
    每一個字元都表示不同 test case 的執行結果。. 表示成功，F 表示失敗（failure），E 表示錯誤（error）。
    
    2. ERROR: test_mod_divide_by_zero (__main__.CalculatorTest)
    逐項列出 test failure/error 的細節。
    
    3. AssertionError: Tuples differ: (2.0, 0) != (1, 0)
    同樣是丟出 AssertionError，但透過 TestCase.assert*() 來做驗證，會產生比較詳細的訊息。
    
    4. FAILED (failures=1, errors=1)
    測試不成功時區分為 test failure （單純是結果與預期不符） 與 test error （執行期發生其他錯誤）。
    
    """
