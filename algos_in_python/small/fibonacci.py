# Multiple solutions to calculate the fibonacci sequence

# Recursion -- Calculates just the next num at given index -- Too big inputs cause trouble as the num of operations rises exponentially
# Index 5 needs 15 calls of fib1 -- Index 10 needs 21.891 calls of fib1
def fib1(n :int) -> int:
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)

if __name__ == '__main__':
    print(fib1(6))