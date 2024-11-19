"""Find a prime number"""

"""1. Any given number 'num' has factors from
the range of base numbers, 1 to 9, if 'num' modulus (%)
these numbers equals zero. 

We know every number is divisble by itself.

A prime number should only be divisble by 1 and itself.


With this number, we aim to..
Step 1: Find all factors of a given number 'num'
Step 2: Check if the factors just two numbers. 1 and itself.
  """


def is_prime(num):
    factors = []
    for fac in range(1,10):
        if num % fac == 0:
            factors.append(fac)
    if num not in factors:
        factors.append(num)
    if len(factors) == 2:
        return True
    else:
        return False
        
"""Replace '7' with any number"""
print(is_prime(7))
            