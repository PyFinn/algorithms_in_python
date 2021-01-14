from typing import Dict
from functools import lru_cache
from typing import Generator

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


# Automated Memoization -- Same result like fib2() with less effort using lru_cache
@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n-1) + fib3(n-2)


# Iterative solution -- Really performant & simple
# For loop executes n - 1 times max.
def fib4(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int  = 1
    for _ in range(1,n):
        last, next = next, last + next
    return next


# Generator -- Return the whole list of fibonacci numbers until the given index -- Uses iteration
def fib5(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1,n):
        last, next = next, last + next
        yield next


if __name__ == '__main__':
    print('The fifth Fibonacci number is {}'.format(fib1(5)))
    print('The twentieth Fibonacci number is {}'.format(fib2(20)))
    print('The thirtieth Fibonacci number is {}'.format(fib3(30)))
    print('The fiftieth Fibonacci number is {}'.format(fib4(50)))
    print('The first fifty Fibonacci numbers:')
    for i in fib5(50):
        print(i)