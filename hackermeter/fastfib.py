"""
Module: fastfib.py
Author: Morgan Strong
Date: 16 August 2013
License: Creative Commons Attribution 3.0 Unported License

The following is a semi-trivial coding example built as a project on 
www.hackermeter.com.  It has been modified slightly for posting.
"""

def fib(n, data={0:0, 1:1, 2:1}):
    """
    Generate the nth element of the fibonacci sequence using Dynamic Programming
    and the Fast-Doubling algorithm, which relies on the following two
    equations:
            
            fib(2k)   = fib(k) * (2fib(k+1) - fib(k))
            fib(2k+1) = fib(k)^2 + fib(k+1)^2
    """
    # Assertions
    if n < 0:
        raise Exception("N must be >= 0.")
    
    # Base Cases
    if n in data:
        return data[n]
    
    # Fast-Doubling Recursion
    k = n/2
    a = fib(k)
    b = fib(k+1)

    if n % 2:
        r = b*b + a*a
    else:
        r = a * (2*b - a)
    
    # Store Results
    # To optimize for space complexity, comment out the two following lines.
    if n not in data:
        data[n] = r

    return r
   

if __name__ == "main":
    print("Print the first N elements of the Fibonacci Sequence.")
    N = raw_input(int(("Enter an integer N > 0:")))
    for i in range(N):
        print(fib(i))
