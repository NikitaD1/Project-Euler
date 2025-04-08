'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91*99
ind the largest palindrome made from the product of two three-digit numbers.

Answer:
993 913 906609
--- 0.27202510833740234 seconds ---
'''

import time, math
start_time = time.time()


def compute():
    maxp = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            product = i*j
            if ispalindrome(product) and product > maxp:
                maxp = product
                factor1, factor2 = i, j

    return factor1,factor2, maxp

def ispalindrome(num):

    end = len(str(num))-1
    numstring = str(num)
    for k in range(len(numstring) // 2):
        if numstring[k]==numstring[end]:
            end = end -1
        else:
            return False

    return True




if __name__ == "__main__":
    i, j, maxp = compute()
    print(i,j, maxp)
    print("--- %s seconds ---" % (time.time() - start_time))