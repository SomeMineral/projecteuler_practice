###############################################################################
# 030 Digit fifth powers
'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
(np.array([1,2,0,3])**2).sum() # oh

# 논리 확인을 위해
def digit_fourth(arg):
    if arg <= 1 or arg != int(arg) :
        return False
    
    temp = arg
    temp_list = []
    while(True):
        temp_list.append(temp % 10)
        temp = temp // 10
        if temp == 0:
            break
    
    sum_fourth = (np.array(temp_list)**4).sum()
    if sum_fourth == arg:
        return True
    else:
        return False

# 999999 -> 9**4 * 6 : 여섯 자리는 안 되겠네.
# 99999 -> 9**4 * 5 : 다섯자리는 가능할 것 같구만.
# 9**4 * n  과 10**(n-1) 을 비교해보는 건가.
# 4 * log2(9) + log2(n) 과 (n-1) * log2(10) 비교.

def maximum_digit_value(arg):
    # 입력값은 전체 자릿수
    n = 1
    while(True):
        comparision_value = arg * np.log2(9) + np.log2(n) - (n-1) * np.log2(10)
        if comparision_value < 0:
            return n
        n += 1

maximum_digit_value(4) # 6. 10**6 까지만 하자.


fourth_sum = 0
for i in range(2, 10**maximum_digit_value(4)):
    if digit_fourth(i):
        print(i)
        fourth_sum += i

print('The sum of all the numbers that can be written as the sum of fourth powers of their digits is:{}'.format(fourth_sum))

# 네 자리 테스트 끝.

def digit_fifth(arg):
    if arg <= 1 or arg != int(arg) :
        return False
    
    temp = arg
    temp_list = []
    while(True):
        temp_list.append(temp % 10)
        temp = temp // 10
        if temp == 0:
            break
    
    sum_fifth = (np.array(temp_list)**5).sum()
    if sum_fifth == arg:
        return True
    else:
        return False

fifth_sum = 0
for i in range(2, 10**maximum_digit_value(5)):
    if digit_fifth(i):
        print(i)
        fifth_sum += i

print('The sum of all the numbers that can be written as the sum of fifth powers of their digits is:{}'.format(fifth_sum))
