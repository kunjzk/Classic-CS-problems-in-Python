# Use memoisation to cache previously computed results. Reduces number of function calls required
# because we can fetch results from memory instead of recomputing them. Note: memo needs to be global.
# Eg: fib(3) = fib(2) + fib(1). memo = {0: 0, 1: 1}. We start from the left.
# fib(2) = fib(1) + fib(0). memo = {0: 0, 1: 1}
# fib(1) = memo[1] = 1
# fib(0) = memo[0] = 0
# fib(2) = 1 + 0 = 1. memo = {0: 0, 1: 1, 2: 1}
# Remember we did left first. So fib(3) = 1 + fib(1)
# fib(1) = memo[1] = 1.
# fib(3) = 1 + 1 = 2. memo = {0: 0, 1: 1, 2: 1, 3: 2}
# Total number of function calls: 5.
# This if you notice is actually the same as fib2. No speedup yet, but we have the added benefit of having cached fib(3).
# Computing fib(4) is much faster now.
# 1. fib(4) = fib(3) + fib(2)
# 2. fib(3) --> 5 calls from earlier, result = 2
# 3. fib(2) --> 1 call, result = 1
# fib(4) = 3
# 7 calls and we're done. Whereas it would have taken 9 calls with fib2.py.
# Going through the same exercise (loop through 0 to 19) we can see the number of calls increments by 2 every time.
# One initial call to the new (incremented n) fib function, and one new call to the fib(n-2) which is cached. 
# fib(n-1) takes the same predictable number of calls to compute.
# Proof is in the pudding:
# 1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37
# An improvement of ~40x!
from typing import Dict


def fib3(n: int, memo: Dict) -> int:
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib3(n-1, memo) + fib3(n-2, memo)
    return memo[n]

NUM_CALLS = 0

def fib3visualize(n: int, memo: Dict) -> int:
    global NUM_CALLS
    NUM_CALLS += 1
    print(memo)
    if n in memo:
        print(f"{NUM_CALLS}: fib3({n}) -> {memo[n]}")
        return memo[n]
    else:
        print(f"{NUM_CALLS}: fib3({n}) -> fib3({n-1}) + fib3({n-2})")
        memo[n] = fib3visualize(n-1, memo) + fib3visualize(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    # print(fib3(5, memo))
    # print(fib3visualize(5, memo))
    # print(NUM_CALLS)
    num_calls_list = []
    for i in range(20):
        NUM_CALLS=0
        memo: Dict[int, int] = {0: 0, 1: 1}
        fib3visualize(i, memo)
        num_calls_list.append(NUM_CALLS)
    print(num_calls_list)