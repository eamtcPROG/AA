import time
import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp

# Algorithm 1: Leibniz Formula
def leibniz_formula(n):
    pi = 0
    for i in range(n):
        pi += ((-1) ** i) / (2 * i + 1)
    return 4 * pi


# Algorithm 2: Bailey–Borwein–Plouffe (BBP) Formula
def bbp_formula(n):
    mp.dps = n + 1
    pi = 0
    for k in range(n):
        pi += (1 / mp.mpf(16) ** k) * ((4 / (8 * k + 1)) - (2 / (8 * k + 4)) - (1 / (8 * k + 5)) - (1 / (8 * k + 6)))
    return pi


# Algorithm 3: Gauss-Legendre Algorithm
def gauss_legendre_algorithm(n):
    mp.dps = n + 1
    a = mp.mpf(1)
    b = 1 / mp.sqrt(2)
    t = 0.25
    p = 1

    for _ in range(n):
        a_next = (a + b) / 2
        b = mp.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    return (a + b) ** 2 / (4 * t)


def analyze_algorithms(n_values):
    algorithms = [leibniz_formula, bbp_formula, gauss_legendre_algorithm]
    timings = [[] for _ in range(len(algorithms))]

    for n in n_values:
        for i, algorithm in enumerate(algorithms):
            start_time = time.time()
            pi = algorithm(n)
            end_time = time.time()
            timings[i].append(end_time - start_time)
            print(f"{algorithm.__name__} (n={n}): {pi}, time: {end_time - start_time:.6f} seconds")
        print(f"---------------------------------------")
    plt.figure(figsize=(10, 6))
    for i, algorithm in enumerate(algorithms):
        plt.plot(n_values, timings[i], label=algorithm.__name__)
    plt.xlabel('Number of Decimal Places (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Performance Comparison of Pi Calculation Algorithms')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    n_values = [100,500,1000,5000,8000]  # Example values for n
    analyze_algorithms(n_values)
