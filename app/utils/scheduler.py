import asyncio

async def schedule_comment(delay, func, *args, **kwargs):
    await asyncio.sleep(delay)
    await func(*args, **kwargs) 