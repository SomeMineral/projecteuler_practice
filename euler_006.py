###############################################################################
# 006 Sum square difference
'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def prob006(num):
    
    sum_sq = sum(range(1, num + 1)) ** 2
    
    sq_sum = 0
    for i in range(1, num + 1 ):
        sq_sum += i**2
    
    return sum_sq - sq_sum


print(prob006(100))
