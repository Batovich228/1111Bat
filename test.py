import unittest
from lesson8 import *
class Test(unittest.TestCase):
    def test_adder(self):
        self.assertEqual(adder(2,2),2)
    def test_adder2(self):
        self.assertEqual(adder(a=10, b=11), 10)

    def test_adder3(self):
        self.assertEqual(adder(1, a=4), 3)

    def test_adder4(self):
        x = 10
        y = 0
        self.assertEqual(adder(0, -5, a=x),5)

    def test_adder5(self):
        self.assertEqual(adder("5", "abc", 10), 10)
if __name__ == '__main__':
    unittest.main()


def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result+=float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result+=int(_)
                continue
            except (ValueError, TypeError):
                pass
    for _ in kwargs.values():
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    return result