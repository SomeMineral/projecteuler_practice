###############################################################################
# 002 Even Fibonacci numbers
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

'''

# million = 10 ** 6

def prob002(num):
    fib = [1,2]
    i = 0
    while(True):
        new_value = fib[i] + fib[i+1]
        i += 1
        if new_value > num:
            break
        fib.append(new_value)
    
    sum = 0
    for i in range(1,len(fib),3):
        sum += fib[i]
    
    return sum

print(prob002(4000000))
    
# even, odd 3개를 주기로 반복됨. 홀 짝 홀 홀 짝 홀 홀 짝...
# list의 index로는 0 1' 2 3 4' 5 6 7' ... => 3k+1 에 해당되는 index
