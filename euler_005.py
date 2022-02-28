###############################################################################
# 005 Smallest multiple
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# 20 이하의 소수 찾고 그것들의 곱한 횟수 찾기?


def prob005(num):
    import math
    prime = []
    # 입력한 값 이하의 소수 모두 찾기
    for i in range(2, num + 1):
        sign = 0
        for j in range(2, int(i**0.5) + 1):
            if (i // j) == (i / j):
                sign = 1
                break
        if sign == 0:
            prime.append(i)
    # 입력한 값 이하의 소수가 최대 몇 번 곱해질 수 있는지 찾기
    mul = 1
    for i in prime:
        mul *= i**int(math.log(num,i))
    return mul

print(prob005(20))
