import unittest


class NumberFactorization:

    def get_factors(self, initial_number):
        for i in range(1, initial_number):
            output = []
            if initial_number % i == 0:
                output.append(i)
        return output
    

class TestGetFactors(unittest.TestCase):
    def setUp(self):
        self.number_factorization = NumberFactorization()

    def test_get_factors_for_prime_number(self):
        self.assertEqual(self.number_factorization.get_factors(7), [1, 7])

    def test_get_factors_for_perfect_square(self):
        self.assertEqual(self.number_factorization.get_factors(25), [1, 5])

    def test_get_factors_for_composite_number(self):
        self.assertEqual(self.number_factorization.get_factors(12), [1, 2, 3, 4, 6, 12])

    def test_get_factors_for_negative_number(self):
        self.assertEqual(self.number_factorization.get_factors(-12), [])

    def test_get_factors_for_zero(self):
        self.assertEqual(self.number_factorization.get_factors(0), [])