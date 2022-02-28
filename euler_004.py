###############################################################################
# 004 Largest palindrome product
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
import math

# 세자리 수 2개 곱의 최소 : 100*100 = 10000, 최대 : 999*999 = 998001
# 대칭인 다섯자리 숫자, 여섯자리 숫자 찾기
pal_num = []
for i in range(10000,100000):
    dig_0 = i % 10
    dig_1 = i // 10 % 10
    dig_3 = i // 1000 % 10
    dig_4 = i // 10000
    if (dig_0 == dig_4) and (dig_1 == dig_3):
        pal_num.append(i)

for i in range(100000,998001+1):
    dig_0 = i % 10
    dig_1 = i // 10 % 10
    dig_2 = i // 100 % 10
    dig_3 = i // 1000 % 10
    dig_4 = i // 10000 % 10
    dig_5 = i // 100000
    
    if (dig_0 == dig_5) and (dig_1 == dig_4) and (dig_2 == dig_3):
        pal_num.append(i)

container = []
for i in pal_num:
    for j in range(100,999+1):
        if (( i // j ) == ( i / j )) and (i != j):
            if ((i//j) // 1000 == 0) and ((i//j) // 100 != 0):
                container.append(i)
                

print(max(container))