#Rebecca Hamid QCC ID:23803320
import unittest
from my_math import is_Prime, Perfect_Square
class TestIsPrimeEdgeCases(unittest.TestCase):

    # Test valid primes and non-primes
    def test_primes_and_nonprimes(self):
        self.assertTrue(isPrime(2))    # smallest prime
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(13))
        self.assertFalse(isPrime(1))   # edge case: 1 is not prime
        self.assertFalse(isPrime(0))   # edge case: 0 is not prime
        self.assertFalse(isPrime(-7))  # negative numbers are not prime
        self.assertFalse(isPrime(4))   # non-prime even number