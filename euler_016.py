###############################################################################
# 016 Power digit sum
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''
num = 2 ** 1000

def prob015(num):
    sub_num = num
    digit_box = []
    while(sub_num != 0):
        digit = sub_num % 10
        sub_num //= 10
        digit_box.append(digit)

    return sum(digit_box)

print(prob015(2**1000)) # 1366