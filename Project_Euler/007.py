'''
A Pythagorean triplet is a set of three natural numbers, a , b , c, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which $a + b + c = 1000. Find the product abc.


Answer:
2516415
'''
import time

start_time = time.time()

def compute(sum_total):
    for a in range(1, sum_total):
        for b in range(a + 1, sum_total - a):
            c = sum_total - a - b
            if a * a + b * b == c * c:
                return a * b * c


if __name__ == "__main__":
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))