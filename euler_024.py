###############################################################################
# 024 Lexicographic permutations
'''
A permutation is an ordered arrangement of objects.
 For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
 If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
 The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import math

## ex>
## 1,2,3,4
## 4! 24
## 3 * 3! + 2 * 2! + 0 * 1! = 22 <<

## 4321 (24) 
## 4312 (23)
## 4231 (22)

## index 그대로. pop(3) 4, [1,2,3]
## index 그대로. pop(2) 3, [1,2]
## index 그대로. pop(0) 1, [2]
## 마지막은 pop() 2, []

## 0~23 : 24개
## 1st ~ 24th : 24개

## 사용할 숫자 22, 실제 순서 23 ( 1의 차이)
## => 앞으로 (실제 순서 - 1)를 사용하자.


num_str = ['{}'.format(i) for i in range(0,10)]
order_num = 1000000
counter = order_num - 1
using_num = list(range(10-1,0,-1))

cnt = 0
factorial_cnt = { i : 0 for i in using_num }

for i in using_num:
    
    change = math.factorial(i)
    while True:
        if counter >= change:
            counter -= change
            cnt += change
            factorial_cnt[i] += 1
        else:
            break
factorial_cnt

perm_str = ''

for i in range(10-1):
    perm_str += num_str.pop(factorial_cnt[10-1-i])

perm_str += num_str.pop()

print(perm_str) # 2783915460