import asyncio
import time

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    url = "http://127.0.0.1:8000/get_student/276"
    num_requests = 1000

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            tasks.append(asyncio.ensure_future(fetch(session, url)))

        start_time = time.time()
        responses = await asyncio.gather(*tasks)
        end_time = time.time()

    print(f"Completed {num_requests} requests in {end_time - start_time:.2f} seconds")
    print(f"Average time per request: {(end_time - start_time) / num_requests:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
