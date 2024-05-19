import numpy as np
import math

PRIME_FACTORIZATION = np.zeros((41, 6))
FACTORIALS_PRIME_FACTORIZATION = np.zeros((41, 6))

primes = {
    2  : 0,
    3  : 1,
    5  : 2,
    7  : 3,
    11 : 4,
    13 : 5
}

rev_primes = inv_map = {v: k for k, v in primes.items()}


for p in primes:
    pp = p
    while pp <= 40:
        temp = pp
        while temp <= 40:
            PRIME_FACTORIZATION[temp][primes[p]] += 1
            temp += pp
        
        pp *= p


for i in range(1, FACTORIALS_PRIME_FACTORIZATION.shape[0]):
   FACTORIALS_PRIME_FACTORIZATION[i] += FACTORIALS_PRIME_FACTORIZATION[i - 1] + PRIME_FACTORIZATION[i]

 
def multiply(num1: np.ndarray, num2: np.ndarray) -> np.ndarray:
    return num1 + num2

def multiplyI(num1: int, num2: int) -> np.ndarray:
    return multiply(PRIME_FACTORIZATION[num1], PRIME_FACTORIZATION[num2])

def divide(num1: np.ndarray, num2: np.ndarray) -> np.ndarray:
    return num1 - num2

def diviveI(num1: int, num2: int) -> np.ndarray:
    return divide(PRIME_FACTORIZATION[num1], PRIME_FACTORIZATION[num2])

def chooseI(num1: int, num2: int) -> np.ndarray:
    if num2 > num1: return np.zeros(FACTORIALS_PRIME_FACTORIZATION.shape[1])
    
    num1_factorial = FACTORIALS_PRIME_FACTORIZATION[num1]
    num2_factorial = FACTORIALS_PRIME_FACTORIZATION[num2]
    difference_factorial = FACTORIALS_PRIME_FACTORIZATION[num1 - num2]
    
    return divide(divide(num1_factorial, num2_factorial), difference_factorial) 

def int_(num: np.ndarray) -> int:
    val = 1
    
    for i, n in enumerate(num):
        val *= math.pow(rev_primes[i], n)

    return val    
