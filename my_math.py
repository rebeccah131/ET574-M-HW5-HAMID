#Rebecca Hamid QCC ID:23803320

#checking if x is a prime number
def is_Prime(x):
    if not isinstance(x, int):
        raise ValueError ("input must be a integer.")
    if x <= 0:              
        return False #x is is less than or equal to 0, which is not a prime number,neither are negative numbers.
    if x == 1:
         return False  #x cannot be 1 since it is not a prime number.
    if x == 2:
        return True   #2 is the only even number that is prime.
    if x  % 2 == 0:
        return False    #even numbers are not prime.
     
     # Check odd divisors up to the square root of x
    limit = 1
    while limit * limit <= x:
        limit += 1
    limit -= 1

    for i in range(3, limit + 1, 2):
        if x % i == 0:
            return False

    return True

#2 Original Math Functions
def Perfect_Square(n):
    if not isinstance(n, int):
        raise ValueError("input must be a integer.")
    if n <= 0:
        return False
    root = int(n ** 0.5)
    return root * root == n




