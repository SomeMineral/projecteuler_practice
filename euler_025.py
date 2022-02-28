###############################################################################
# 025 1000-digit Fibonacci number
'''
The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

def is1000digits(arg):
    import math
    if 999 <= math.log10(arg) < 1000:
        return True
    else:
        return False

fib_list = [1, 1]
idx = 2 
while True:
    idx += 1
    fib_list.append(fib_list[0] + fib_list[1])
    fib_list.pop(0) # 이전 값 제거.
    if is1000digits(fib_list[1]):
        break
    
print(idx)