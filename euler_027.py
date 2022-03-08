###############################################################################
# 027 Quadratic primes
'''
Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
However, when n = 40, 40**2 + 40 + 41 = 40*(40 + 41) + 41 is divisible by 41,
and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula n**2 - 79*n + 1601 was discovered, which produces 80 primes for the consecutive values
0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n**2 + a*n + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b,
 for the quadratic expression that produces the maximum number of primes for consecutive values of n,
 starting with n = 0.
'''

# coefficient 만들어서 전부 저장하기엔 메모리 많이 차지하는 것 같아서 generator 찾아봄. yield 오랜만에 보네.

def coeff_gen(x,y):
    for i in range(-x, x):
        for j in range(-y, y + 1):
            yield (i,j)

[ (i,j,1) for i,j in coeff_gen(2,2) ] # test

def quadratics(a, b, n):
    return n**2 + a*n + b

def Isprime(arg):
    if arg != int(arg) or arg <= 1:
        return False
    # 한 자리수 prime은 그냥 입력해둘게요.
    if arg in [2,3,5,7]:
        return True
    
    for i in range(2, int(arg**0.5) + 1):
        temp = arg / i
        if temp == int(temp):
            return False  
    return True

def multiply_2(x,y):
    return x * y

multiply_2(*(3,6))

max_n = 0
coeff = (-1000,-1000)

for i,j in coeff_gen(1000,1000):
    n = 0
    marker = 0
    while(True):
        if Isprime(quadratics(i, j, n)):
            n += 1
            continue
        else:
            break
    if n > max_n:
        max_n = n
        coeff = (i,j)
        print('n = {}, a = {}, b = {}'.format(n,i,j))

print('n = {}, a * b = {}'.format(max_n, multiply_2(*coeff))) # -59231
