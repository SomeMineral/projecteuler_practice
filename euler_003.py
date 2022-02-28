###############################################################################
# 003 Largest prime factor
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

def prob003(num):
    max_rng = int(num**0.5)
    # 약수 찾기 ( 1 제외 )
    container = []
    if max_rng **2 == num:
        container.append(max_rng)

    for i in range(2,max_rng):
        if (num / i) == (num // i):
            container.append(i)
            container.append(num // i)

    print('약수 (1, 자신 제외) : {}'.format(container))

    container_2 = []            
    for i in container:
        sign = 0
        for j in range(3,i):
            if (i // j) == (i / j):
                sign = 1
                break
        if sign == 0:
            container_2.append(i)
    
    print('약수 중에 소수 : {}'.format(container_2))
    
    return(max(container_2))

print(prob003(600851475143))