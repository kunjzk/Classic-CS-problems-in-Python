# Has a base case, if n = 0 return 0, if n=1 return 1
# Problem: Every call to fib2 results in 2 more calls to fib2, even if that sum has already been computed.
# As a result the number of calls to fib2 grows exponentially with n.
# Printing out number of calls to fib2 as n grows from 0 to 19:
# 1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219, 1973, 3193, 5167, 8361, 13529
# 13k calls to the function to compute the value of fib(19)!
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

NUM_CALLS = 0

def fib2visualize(n: int) -> int:
    global NUM_CALLS
    NUM_CALLS += 1
    if n < 2:
        print(f"{NUM_CALLS}: fib2({n}) -> {n}")
        return n
    print(f"{NUM_CALLS}: fib2({n}) -> fib2({n-1}) + fib2({n-2})")
    return fib2visualize(n-1) + fib2visualize(n-2)

if __name__ == "__main__":
    #print(fib2(5))
    #print(fib2visualize(6))
    num_calls_list = []
    for i in range(20):
        NUM_CALLS=0
        fib2visualize(i)
        num_calls_list.append(NUM_CALLS)
    print(num_calls_list)