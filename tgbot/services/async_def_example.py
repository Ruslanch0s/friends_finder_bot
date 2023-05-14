import asyncio
import concurrent.futures


# ---------   При работе с requests библиотекой   ---------
# import requests as requests
# import aiohttp
# async def get(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()


# ---------   Любая другая блокирующая функция (например бд)   ---------
# async def sync_to_async(url):
#     response = await run_blocking_io(requests.get, url)
#     return response.text

# Вызывать через sync_to_async
async def run_blocking_io(func, *args):
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, func, *args
        )
    return result
