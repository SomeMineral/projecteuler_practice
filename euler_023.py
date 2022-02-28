###############################################################################
# 023 Non-abundant sums
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
 which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and
 it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
 the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
 even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

def isabundant(arg):
    if arg != int(arg) or arg <= 1:
        return False

    prop_div_list = [1]
    for i in range(2, int(arg**0.5) + 1):
        temp = (arg / i)
        if temp == int(temp):
            prop_div_list.append(temp)
            if temp ** 2 != arg:
                prop_div_list.append(int(arg / temp))
    if sum(prop_div_list) > arg:
        return True
    else:
        return False


non_two_abundant = []
for i in range(1,28123):
    checker = 0
    for j in range(1,i):
        if isabundant(j) and isabundant(i - j):
            checker = 1
            break
    if checker == 0:
        non_two_abundant.append(i)

print(sum(non_two_abundant)) # 4179871