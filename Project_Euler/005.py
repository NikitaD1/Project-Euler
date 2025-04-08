'''
Euler Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer:

'''

import math

# Function to find the Least Common Multiple (LCM) of two numbers
def lcm(a, b):
    return a * b // math.gcd(a, b)

# Function to find the LCM of numbers from 1 to n
def find_smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

if __name__ == "__main__":
    # We need the smallest multiple of numbers from 1 to 20
    smallest_multiple = find_smallest_multiple(20)
    print(smallest_multiple)
