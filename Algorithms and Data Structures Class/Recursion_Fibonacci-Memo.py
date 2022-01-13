def fib(n,memo):
    if n ==0: 
        return 0
    if memo[n] != None: #then we have already stored the value
        return memo[n]
    if n ==1 or n==2:
        result =1
    else: 
        result = fib((n-1),memo) + fib((n-2),memo)
    memo[n] = result
    return result
    
# Test cases
memo = [None] * 10
print fib(9,memo)
memo = [None] * 12 
print fib(11,memo)
memo = [None] * 1
print fib(0,memo)
