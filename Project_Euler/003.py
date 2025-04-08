'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Answer:
    6857
--- 0.0002269744873046875 seconds ---

'''

import time, math
start_time = time.time()


def compute(number):
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            number //= factor
        else:
            factor += 1
    return number


if __name__ == "__main__":
    print(compute(600851475143))
    print("--- %s seconds ---" % (time.time() - start_time))