import unittest
import Calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = Calc.add(10,5)
        self.assertEqual(result,15)
        self.assertEqual(Calc.add(-1,-1),-2)
        self.assertEqual(Calc.add(-1, 1), 0)

    def test_mul(self):
        result = Calc.mul(10, 5)
        self.assertEqual(result, 50)

    def test_div(self):
        result = Calc.div(5,2)
        self.assertEqual(result,2.5)
        self.assertRaises(ValueError,Calc.div, 10,0)
        with self.assertRaises(ValueError):
            Calc.div(10,0)


if __name__ == '__main__':
    main()
