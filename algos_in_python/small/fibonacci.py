from typing import Dict

# Multiple solutions to calculate the fibonacci sequence

# Recursion -- Calculates just the next num at given index -- Too big inputs cause trouble as the num of operations rises exponentially
# Index 5 needs 15 calls of fib1 -- Index 20 needs 21.891 calls of fib1
def fib1(n :int) -> int:
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)


# Memoization -- More effective than fib1 as the function memorizes the result of operations
# Index 20 now needs only 39 calls
memory: Dict[int, int] = {0: 0, 1: 1}
def fib2(n :int) -> int:
    if n not in memory:
        memory[n] = fib2(n-1) + fib2(n-2) # Memoization
    return memory[n]

if __name__ == '__main__':
    print(fib1(5))
    print(fib2(20))