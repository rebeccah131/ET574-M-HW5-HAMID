#Rebecca Hamid QCC ID:23803320
import unittest
from my_math import is_Prime, Perfect_Square
class TestIsPrimeEdgeCases(unittest.TestCase):

    # Test valid primes and non-primes
    def test_primes_and_nonprimes(self):
        self.assertTrue(is_Prime(2))    # smallest prime
        self.assertTrue(is_Prime(3))
        self.assertTrue(is_Prime(13))
        self.assertFalse(is_Prime(1))   # edge case: 1 is not prime
        self.assertFalse(is_Prime(0))   # edge case: 0 is not prime
        self.assertFalse(is_Prime(-7))  # negative numbers are not prime
        self.assertFalse(is_Prime(4))   # non-prime even number

 # Test invalid inputs
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            is_Prime("7")    # string input

        with self.assertRaises(ValueError):
            is_Prime(3.14)   # float input

        with self.assertRaises(ValueError):
            is_Prime([])     # empty list

        with self.assertRaises(ValueError):
            is_Prime([2,3])  # non-empty list

        with self.assertRaises(ValueError):
            is_Prime(None)   # None input

# Run the tests if this file is executed
if __name__ == "__main__":
    unittest.main()

#unit test for perfect square

# Your Perfect_Square function
def Perfect_Square(n):
    if not isinstance(n, int):
        raise ValueError("input must be a integer.")
    if n <= 0:
        return False
    root = int(n ** 0.5)
    return root * root == n


class TestPerfectSquare(unittest.TestCase):

    # Test 1: Edge cases
    def test_edge_cases(self):
        self.assertFalse(Perfect_Square(0))      # 0 is not a perfect square
        self.assertTrue(Perfect_Square(1))       # 1 is a perfect square
        self.assertFalse(Perfect_Square(-4))     # negative numbers
        self.assertTrue(Perfect_Square(16))      # small perfect square
        self.assertFalse(Perfect_Square(20))     # not a perfect square
        self.assertTrue(Perfect_Square(1000000)) # large perfect square

    # Test 2: Invalid inputs
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            Perfect_Square("16")    # testing a string input

        with self.assertRaises(ValueError):
            Perfect_Square(16.0)    # testing float input

        with self.assertRaises(ValueError):
            Perfect_Square([])      # checking for an empty list

        with self.assertRaises(ValueError):
            Perfect_Square(None)    # check if there is no input

# Run tests
if __name__ == "__main__":
    unittest.main()


# Your is_perfect_number function
def is_perfect_number(n):
    """
    Returns True if n is a perfect number, otherwise False.

    Edge cases:
    - n <= 0 → raises ValueError
    - non-integer input → raises ValueError
    """

    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


class TestPerfectNumber(unittest.TestCase):

    # Test 1: Edge cases
    def test_edge_cases(self):
        self.assertTrue(is_perfect_number(6))   # smallest perfect number
        self.assertTrue(is_perfect_number(28))  # another perfect number
        self.assertFalse(is_perfect_number(12)) # not perfect
        self.assertFalse(is_perfect_number(1))  # edge case: 1 is not perfect
        self.assertFalse(is_perfect_number(2))  # 2 is not perfect

    # Test 2: Invalid inputs
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            is_perfect_number(-6)    # negative number

        with self.assertRaises(ValueError):
            is_perfect_number(3.5)   # float input

        with self.assertRaises(ValueError):
            is_perfect_number("28")  # string input

        with self.assertRaises(ValueError):
            is_perfect_number([])    # empty list
