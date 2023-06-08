import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_divide(self):

        self.assertEqual(self.calculator.divide(10, 5), 2)
        self.assertEqual(self.calculator.divide(-10, 5), -2)
        self.assertEqual(self.calculator.divide(10, -5), -2)
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 10, 0)
        self.assertRaises(TypeError, self.calculator.divide, 10, "5")
        self.assertRaises(TypeError, self.calculator.divide, "10", 5)
        self.assertRaises(TypeError, self.calculator.divide, 'a', 6)
        self.assertRaises(TypeError, self.calculator.divide, 'f', '6')

    def test_multiply(self):

        self.assertEqual(self.calculator.multiply(10, 5), 50)
        self.assertEqual(self.calculator.multiply(-10, 5), -50)
        self.assertEqual(self.calculator.multiply(10, -5), -50)
        self.assertRaises(TypeError, self.calculator.multiply, 10, "5")
        self.assertRaises(TypeError, self.calculator.multiply, "10", 5)
        self.assertRaises(TypeError, self.calculator.multiply, 'a', 6)
        self.assertRaises(TypeError, self.calculator.multiply, 'f', '6')

    def test_sum(self):

        self.assertEqual(self.calculator.sum(10, 5), 15)
        self.assertEqual(self.calculator.sum(-10, 5), -5)
        self.assertEqual(self.calculator.sum(10, -5), 5)
        self.assertRaises(TypeError, self.calculator.sum, 10, "5")
        self.assertRaises(TypeError, self.calculator.sum, "10", 5)
        self.assertRaises(TypeError, self.calculator.sum, 'a', 6)
        # self.assertRaises(TypeError, self.calculator.sum, 'f', '6')

    def test_subtract(self):

        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-10, 5), -15)
        self.assertEqual(self.calculator.subtract(10, -5), 15)
        self.assertRaises(TypeError, self.calculator.subtract, 10, "5")
        self.assertRaises(TypeError, self.calculator.subtract, "10", 5)
        self.assertRaises(TypeError, self.calculator.subtract, 'a', 6)
        self.assertRaises(TypeError, self.calculator.subtract, 'f', '6')
    
    def test_stdev(self):
        numbers = [10, 12, 15, 14, 13, 11, 9, 10, 12, 14]
        numbers2 = [1]
        self.assertEqual(self.calculator.calculate_stdev(numbers), 2.0)
        self.assertRaises(TypeError, self.calculator.calculate_stdev, 'a' )
        self.assertRaises(ValueError, self.calculator.calculate_stdev, numbers2)
        self.assertRaises(TypeError, self.calculator.calculate_stdev, 4 )
    
    def test_mean(self):
        numbers = [10, 12, 15, 14, 13, 11, 9, 10, 12, 14]
        self.assertEqual(self.calculator.calculate_average(numbers), 12.0)
        self.assertRaises(TypeError, self.calculator.calculate_average, 'a' )
        self.assertRaises(TypeError, self.calculator.calculate_average, 4 )

    def test_var(self):
        numbers = [10, 12, 15, 14, 13, 11, 9, 10, 12, 14]
        numbers2 = [2]
        self.assertEqual(self.calculator.calculate_var(numbers), 4.0)
        self.assertRaises(TypeError, self.calculator.calculate_var, 'a' )
        self.assertRaises(TypeError, self.calculator.calculate_var, 5)
        self.assertRaises(TypeError, self.calculator.calculate_var, 8.4)
        self.assertRaises(ValueError, self.calculator.calculate_var, numbers2)
        self.assertRaises(TypeError, self.calculator.calculate_var, 4 )
    
    def test_zscore(self):
        numbers = [10, 12, 15, 14, 13, 11, 9, 10, 12, 14]
        x = 13
        self.assertEqual(self.calculator.calculate_z_score(x,numbers), 0.5)
        self.assertRaises(TypeError, self.calculator.calculate_z_score, 'a', numbers )
        self.assertRaises(TypeError, self.calculator.calculate_z_score, 13, "a")
        self.assertRaises(TypeError, self.calculator.calculate_z_score, "a", 3)





if __name__ == "__main__":
    unittest.main()