#!/usr/bin/env python

from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

from task import task


def pool(count: int) -> float:
    start = perf_counter()
    with ProcessPoolExecutor() as executor:
        for t in executor.map(task, [6000 for _ in range(count)]):
            print("task:", t)
    end = perf_counter()
    return end - start


if __name__ == "__main__":
    n = 32
    total = pool(n)
    print("total:", total)
    print("mean:", total / n)
