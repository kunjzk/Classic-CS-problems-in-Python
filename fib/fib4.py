# Use python magic to automate what we did in fib3.
# A decorator that automatically caches the return value of fib4() when it is called with a specific argument.
# Note: this is even faster because it caches the function call + argument. So we don't even need to enter the function to get a value out!
# Number of calls with inputs 0 to 19:
# 1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n <2:
        return n
    return fib4(n-1) + fib4(n-2)

NUM_CALLS = 0

@lru_cache(maxsize=None)
def fib4visualize(n: int) -> int:
    global NUM_CALLS
    NUM_CALLS += 1
    if n <2:
        print(f"{NUM_CALLS}: fib4({n}) -> {n}")
        return n
    print(f"{NUM_CALLS}: fib4({n}) -> fib4({n-1}) + fib4({n-2})")
    return fib4visualize(n-1) + fib4visualize(n-2)

# def fib3visualize(n: int, memo: Dict) -> int:
#     global NUM_CALLS
#     NUM_CALLS += 1
#     print(memo)
#     if n in memo:
#         print(f"{NUM_CALLS}: fib3({n}) -> {memo[n]}")
#         return memo[n]
#     else:
#         print(f"{NUM_CALLS}: fib3({n}) -> fib3({n-1}) + fib3({n-2})")
#         memo[n] = fib3visualize(n-1, memo) + fib3visualize(n-2, memo)
#     return memo[n]

if __name__ == "__main__":
    # print(fib4(5))
    # print(fib4visualize(5))
    num_calls_list = []
    for i in range(20):
        NUM_CALLS=0
        fib4visualize.cache_clear()
        fib4visualize(i)
        num_calls_list.append(NUM_CALLS)
    print(num_calls_list)