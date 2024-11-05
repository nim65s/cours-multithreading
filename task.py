#!/usr/bin/env python
from time import perf_counter

import numpy as np


def task(size: int = 6000) -> float:
    a = np.random.rand(size, size)
    b = np.random.rand(size)

    start = perf_counter()
    _x = np.linalg.solve(a, b)
    end = perf_counter()
    return end - start


if __name__ == "__main__":
    print("task:", task())
