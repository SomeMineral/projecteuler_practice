###############################################################################
# 020 Factorial digit sum
'''
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
'''

def digit_sum(arg):
    if arg != int(arg) or arg <= 0:
        return
    temp_num = arg
    d_sum = 0
    while True:
        d_sum += temp_num % 10
        temp_num //= 10
        if temp_num < 10:
            d_sum += temp_num
            return d_sum 

import math

print(digit_sum(math.factorial(100))) # 648