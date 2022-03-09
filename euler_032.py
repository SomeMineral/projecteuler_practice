###############################################################################
# 032 Pandigital products
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
 for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
 containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
# case 1. OO x OOO = OOOO
# case 2. O x OOOO = OOOO 

from itertools import permutations

pan_list = []

for i in permutations(range(1,10),9):
    temp = (10 * i[0] + i[1], 100 * i[2] + 10 * i[3] + i[4], 1000 * i[5] + 100 * i[6] + 10 * i[7] + i[8])
    if temp[0] * temp[1] == temp[2]:
        pan_list.append(temp)
    temp = (i[0], 1000 * i[1] + 100 * i[2] + 10 * i[3] + i[4], 1000 * i[5] + 100 * i[6] + 10 * i[7] + i[8])
    if temp[0] * temp[1] == temp[2]:
        pan_list.append(temp)

product_list = [i[2] for i in pan_list]
sum(set(product_list)) # 45228