#Rebecca Hamid QCC ID:23803320

#checking if x is a prime number
def is_Prime(x):
    try:
        x = int(x)
    except: 
            ValueError("x has to be an integer.")

if x <= 1:              
    return False   #x is is less than or equal to 1, which is not a prime number,neither are negative numbers.
if x % 2 == 0:
    return False   #even numbers are not prime numbers



    