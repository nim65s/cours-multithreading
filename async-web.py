#!/usr/bin/env python
import asyncio
from time import perf_counter

import httpx

URL = "https://www.laas.fr"
KNOWN = set()
CUMUL = 0


async def get(url: str, client: httpx.AsyncClient):
    global URL, KNOWN, CUMUL
    print(f"get {url=}")
    start = perf_counter()

    r = None
    while r is None:
        try:
            r = await client.get(URL + url)
        except Exception:
            print(f"try again {url=}")

    end = perf_counter()
    CUMUL += end - start
    KNOWN.add(url)
    content = r.content.decode()
    tasks = []
    for url in content.split('"'):
        if url.startswith("/fr/") and url not in KNOWN:
            tasks.append(asyncio.create_task(get(url, client)))

    for task in tasks:
        await task


async def async_web() -> float:
    global URL, KNOWN, CUMUL
    start = perf_counter()

    async with httpx.AsyncClient() as client:
        await get("/fr/", client)

    end = perf_counter()
    return end - start


if __name__ == "__main__":
    print("temps écoulé:", asyncio.run(async_web()))
    print("temps cumulé:", CUMUL)
