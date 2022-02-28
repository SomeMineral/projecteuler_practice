###############################################################################
# 010 Summation of primes
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

def prob010(num):  
    prime_sum = 0
    for i in range(2,num):
        sign = 0
        for j in range(2,int(i**0.5)+1):
            if (i//j) == (i/j):
                sign = 1
                break
        if sign == 0:
            prime_sum += i

    return prime_sum
        

print(prob010(2000000)) # 142913828922