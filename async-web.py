#!/usr/bin/env python
import asyncio
from time import perf_counter

import httpx

URLS = [
    "https://www.upssitech.eu/",
    "https://www.upssitech.eu/formation/departement-genie-civil-geotechnique-gcgeo/",
    "https://www.upssitech.eu/presentation/vie-etudiante/",
]


async def async_web() -> float:
    start = perf_counter()

    async with httpx.AsyncClient() as client:
        for url in URLS:
            await client.get(url, timeout=20.0)

    end = perf_counter()
    return end - start


if __name__ == "__main__":
    print(asyncio.run(async_web()))
