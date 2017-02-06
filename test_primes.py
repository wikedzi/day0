import unittest
from primes import primeNumbers

class PrimeFunction(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertEqual(primeNumbers(2,10), [2,3,5,7])

if __name__ == '__main__':
    unittest.main()
