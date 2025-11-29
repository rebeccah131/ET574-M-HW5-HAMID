#Rebecca Hamid QCC ID:23803320

#checking if x is a prime number
def is_Prime(x):
    try:
        x = int(x)
    except: 
            ValueError("x has to be an integer.")

    if x <= 0:              
        return False #x is is less than or equal to 0, which is not a prime number,neither are negative numbers.
    if x == 1:
         return False  #x cannot be 1 since it is not a prime number.
    if x % 2 == 0:
        return False   #even numbers are not prime numbers
    if x  == 2:
        return True    #2 is the only even number that is a prime number.

#2 Original Math Functions
def Perfect_Square(n):
    try: 
         n = int(n)
    except: ValueError("n had to be an integer.")
    if n <= 0:
        return False
    root = int(n ** 0.5)
    return root * root == n




