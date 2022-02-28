###############################################################################
# 001 Multiples of 3 or 5

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

# 3의 배수 + 5의 배수 - 15의 배수

def prob001(num):
    # only below this number
    cnt_3 = (num - 1) // 3
    cnt_5 = (num - 1) // 5
    cnt_15 = (num - 1) // 15
    
    return 3 * sum(range(1 , cnt_3 + 1)) + 5 * sum(range(1 , cnt_5 + 1)) - 15 * sum(range(1 , cnt_15 + 1))

print(prob001(1000))
