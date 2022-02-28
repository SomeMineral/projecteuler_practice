###############################################################################
# 021 Amicable numbers
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
 therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
'''
def proper_divisors(arg):
    if arg != int(arg) or arg <= 0:
        return
    div_list = [1]
    for i in range(2,int(arg**0.5)+1):
        div_num = arg / i
        if div_num == int(div_num):
            div_list.append(i)
            if div_num != i:
                div_list.append(int(div_num))
    return div_list

sum(proper_divisors(220))
sum(proper_divisors(284))


amicable_num_sum = 0
for i in range(1,10000):
    n = sum(proper_divisors(i))
    m = sum(proper_divisors(n))
    if m == i and n != i:
        amicable_num_sum += i

print(amicable_num_sum) # 31626