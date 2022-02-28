###############################################################################
# 015 Lattice paths
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
(그림 생략)
How many such routes are there through a 20×20 grid?
'''
# 어.. 이건 그냥 단순 수학 문제. 고등학교 수학 최단거리 구하기 문제.
import math
math.factorial(40)/(math.factorial(20)**2)
