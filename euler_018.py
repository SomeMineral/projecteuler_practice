###############################################################################
# 018 Maximum path sum I
'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
 the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
'''

tri = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

import copy
import math
import numpy as np

seq = tri.split('\n')
seq1 = [i.split(' ') for i in seq]
# 마지막 줄의 길이와 전체 높이는 동일하다!

# 모든 행의 길이를 마지막 행과 맞춰주기 위해서 0을 채워넣기.
height = len(seq1)
for i in range(height):
    for j in range(height-1-i):
        seq1[i].append(0)

# array로 생성하면서 숫자 0과 삼각형 내의 문자의 형식을 정수로 통일.
seq_f = np.array(copy.deepcopy(seq1)).astype('int64')

# np.binary_repr(10,15)

max_total = 0
routes = int(math.pow(2,height-1))
for i in range(routes):
    route_bin = np.binary_repr(i,height) # 경로 선택은 14번 하지만, 전체 숫자는 15개이므로 일단 15개로 자릿수 맞춰줄게.
    col = 0
    tot = seq_f[0,0] # 첫번째 층 (zero index row)은 고정값
    for j in range(1,height):
        idx_change = int(route_bin[j])
        col += idx_change
        tot += seq_f[j, col]
    
    print('route_bin {} - total {}'.format(route_bin, tot))
    if max_total < tot:
        max_total = tot
    
print(max_total) # 1074