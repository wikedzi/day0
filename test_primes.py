import unittest
from primes import primeNumbers

class PrimeFunction(unittest.TestCase):
    
    def test_prime_numbers(self):
        self.assertEqual(primeNumbers(2,10), [2,3,5,7])
    
    def test_is_greater_than_zero(self):
        self.assertTrue(primeNumbers(2,10)!=102)

    def test_start_is_greater_than_end(self):
        self.assertTrue(primeNumbers(2,10)!=101)

if __name__ == '__main__':
    unittest.main()
