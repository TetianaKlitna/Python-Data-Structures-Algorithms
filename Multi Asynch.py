import asyncio
async def sum(n1, n2):
    await asyncio.sleep(1)
    return n1 + n2

# Create event loop
loop = asyncio.get_event_loop()

async def when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print('Result:', await res)

loop.run_until_complete(when_done([
    sum(1, 9),
    sum(2, 10),
    sum(3, 7)
]))