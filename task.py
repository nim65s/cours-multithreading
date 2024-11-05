from time import perf_counter

import numpy as np


def task(size=6000):
    a = np.random.rand(size, size)
    b = np.random.rand(size)

    start = perf_counter()
    _x = np.linalg.solve(a, b)
    end = perf_counter()
    print(end - start)


if __name__ == "__main__":
    task()
