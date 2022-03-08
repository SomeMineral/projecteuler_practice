###############################################################################
# 028 Number spiral diagonals
'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
# 껍질? 의 개수를 n이라 하면 사각형의 한 변의 길이는 2n-1 => (변의 길이 + 1) / 2 = 껍질 개수
# 우측 상단의 값은 반드시 제곱값. 껍질 번호를 k라 하면 우측 상단의 값은 (2k-1)**2
# 각 귀퉁이 값은 제곱값을 기준으로 변의 길이를 이용해서 계산해볼 수 있음.
# ex) 25 = 5**2 에서 왼쪽으로 쭈욱 가면 21 = 5**2 - 5 + 1
# 25에서 왼쪽으로 쭈욱 아래로 쭈욱 가면 17 = 5**2 - 5 + 1 - 5 + 1
# 25에서 왼쪽으로 쭈욱 아래로 쭈욱 오른쪽으로 쭈욱 가면 13 = 5**2 - 5 + 1 - 5 + 1 - 5 + 1

#(2k-1)**2 - (2k-1) + 1 ..... (2k-1)**2
# ......................................
#(2k-1)**2 - 2*(2k-1) + 2*1 ...... (2k-1)**2 - 3*(2k-1) + 3*1

# 즉, 껍질 하나당 네 귀퉁이 총 합은 4 * (2k-1)**2 -6*(2k-1) + 6*1 = 16 * k**2 -28*k + 16
# 단, k >=2 일 때.

# 028, 껍질 개수 = (1001 - 1) / 2 = 500
# 따라서 500개의 껍질. 

length = 1001
sum = 1 # 가장 가운데 1은 한 개 값.
for i in range(2, int((length+1)/2) +1):
    print((16 * (i**2) - 28 * i + 16))
    sum += (16 * (i**2) - 28 * i + 16) 

print(sum) #669171001