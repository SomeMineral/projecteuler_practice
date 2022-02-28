###############################################################################
# 014 Longest Collatz sequence
'''
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def prob014(num):
    maximum_chain = 1
    maximum_chain_number = 0
    
    def collatz_chain_length(num):     

        def iter_comp(n):
            if n == 1:
                return False
            if n % 2 == 0:
                return n/2
            if n % 2 == 1:
                return 3*n + 1
   
        seq_idx = 1
        if num == 1:
            return 1
        seq_val = num  
        
        while(seq_val != 1):
            seq_idx += 1
            seq_val = iter_comp(seq_val)
        
        return seq_idx
    
    for i in range(1,num):
        sub_chain = collatz_chain_length(i)
        if maximum_chain < sub_chain:
            maximum_chain = sub_chain
            maximum_chain_number = i
                
    return maximum_chain_number

print(prob014(1000000))