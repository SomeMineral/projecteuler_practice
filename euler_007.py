###############################################################################
# 007 10001st prime
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

test_num = 150000
prime = []
for i in range(2,test_num + 1):
    sign = 0
    for j in range(2, int(i**0.5) + 1):
        if (i // j) == (i / j):
            sign = 1
            break
    if sign == 0:
        prime.append(i)

print(prime[10000]) # 10001th