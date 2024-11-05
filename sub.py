#!/usr/bin/env python
from subprocess import Popen
from time import perf_counter


def sub(count: int) -> float:
    start = perf_counter()

    processes = [Popen(["./task.py"]) for _ in range(count)]

    for p in processes:
        p.wait()
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    n = 16
    total = sub(n)
    print("total:", total)
    print("mean:", total / n)
