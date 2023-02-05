import time
import matplotlib.pyplot as plt
import math

def Fib(n):
    if n <= 1:
        return n
    else:
        return Fib(n-1) + Fib(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

def fibonacci_dynamic(n, memo={}):
    if n<=1:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_dynamic(n-1, memo) + fibonacci_dynamic(n-2, memo)
        return memo[n]

def multiply(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C

def power(A, n):
    if n <= 1:
        return A
    else:
        B = power(A, n//2)
        C = multiply(B, B)
        if n % 2 == 0:
            return C
        else:
            return multiply(C, A)

def fibonacci_matrix(n):
    if n<=1:
        return n
    else:
        F = [[1, 1], [1, 0]]
        F_n = power(F, n-1)
        return F_n[0][0]

def fibonacci_recurrence_matrix(n):
    if n<=1:
        return n
    else:
        F = [[1, 1], [1, 0]]
        F_n = multiply(F, [[1, 1], [1, 0]])
        for i in range(2, n):
            F_n = multiply(F_n, F)
        return F_n[0][0]

def fibonacci_closed_form(n):
    if n<=1:
        return n
    else:
        golden_ratio = (1 + math.sqrt(5)) / 2
        return int(round((golden_ratio**n - (1 - golden_ratio)**n) / math.sqrt(5)))

def createGraph(n,Fib):
    x = list(range(n))
    y = []
    t = []
    for i in range(n):
        start_time = time.time()
        Fib(i)
        end_time = time.time()
        y.append(Fib(i))
        t.append(end_time - start_time)

    plt.plot(x, t)
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Time needed to calculate Fibonacci numbers")
    plt.show()

def printTable(n,Fib):
    max_value = Fib(n - 1)
    num_digits = len(str(max_value))
    max_width = max(4, num_digits)
    if n < 0:
        print("n should be > 0")
    else:
        for i in range(n):
            print("{:^{}}".format(i + 1, max_width), end="|")
        print("\n", end="")
        for i in range(n):
            print("{:^{}}".format(Fib(i), max_width), end="|")
        print("\n", end="")
        for i in range(n):
            start_time = time.time()
            Fib(i)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("{:^{}.2f}".format(elapsed_time, max_width), end="|")
        createGraph(n,Fib)

if __name__ == '__main__':
    n = int(input("Enter the n: "))
    print("Fibonacci sequence Recursive method")
    printTable(n,Fib)
    n = int(input("\nEnter the n: "))
    print("\nFibonacci sequence Iterative method")
    printTable(n, fibonacci_iterative)
    print("\nFibonacci sequence Dynamic programming")
    printTable(n, fibonacci_dynamic)
    print("\nFibonacci sequence Matrix recurrence")
    printTable(n, fibonacci_recurrence_matrix)
    print("\nFibonacci sequence Matrix exponentiation")
    printTable(n, fibonacci_matrix)
    print("\nFibonacci sequence Closed-form expression")
    printTable(n, fibonacci_closed_form)
