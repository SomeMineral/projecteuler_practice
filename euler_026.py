###############################################################################
# 026 Reciprocal cycles
'''

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:
    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

# 와. 이틀 고민해도 안 되더니.. 접근 방식 자체가 다르구나.
# 으으. 검색해봤다. 이건 좀 너무하다!

'''
1 // 7 = 0 ( 정수 자리 ) , 1 % 7 = 1 (나머지)
1*10 // 7 = 1 (소수 첫째 자리), 1*10 % 7 = 3 (나머지)
3 * 10 // 7 = 4 (소수 둘째 자리), 3*10 % 7 = 2 (나머지)
...

diviend (나눠지는 수)
divisor (나누는 수)
quotient (몫)
remainder (나머지)
'''

decimal_list = [] # (소수 x째 자리 숫자 , 연산 당시 나머지) tuple 형태로 저장해보자.
# 0번째 : 정수 부분
# 몫과 나머지가 완벽하게 동일한 순간이 찾아오면 그 때가 순환 시작.

def cycle_finder(divisor):
    decimal_list = []
    remainder = 1
    cycle_length = 0
    while True:
        decimal_list.append((remainder // divisor, remainder % divisor))
        remainder = 10 * (remainder % divisor)
        if decimal_list[-1] in decimal_list[0:-1]:
            cycle_length = len(decimal_list) - decimal_list.index(decimal_list[-1]) - 1
            break
        if decimal_list[-1] == (0,0): # 몫도 나눌 것도 없으면 유한 소수니까...
            break
    return cycle_length

max_len = 0
value = 2
for i in range(2, 1000):
    cycle_len = cycle_finder(i)
    print('i = {}, cycle_len : {}'.format(i,cycle_len))
    
    if cycle_len > max_len:
        max_len = cycle_len
        value = i
print('d = {}, max_len = {}'.format(value, max_len))


