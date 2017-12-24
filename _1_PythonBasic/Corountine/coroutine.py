import asyncio

@asyncio.coroutine
async def example():
    await asyncio.sleep(5)
    return 5

if __name__ == '__main__':
    scheduler = asyncio.get_event_loop()
    f = asyncio.async(example())
    f2 = asyncio.async(example(),loop= scheduler)

