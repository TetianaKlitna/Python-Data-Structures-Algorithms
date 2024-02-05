import asyncio

async def sum(n1,n2):
    print('Sum numbers', n1, '+', n2)
    await asyncio.sleep(1)
    print('End Sum', n1, '+', n2)
    return n1 + n2

# Create event loop
loop = asyncio.get_event_loop()
n1 = 1
n2 = 2
# Run async function and wait for completion
results = loop.run_until_complete(sum(n1, n2))
print("Sum of two numbers:", n1, "+", n2, "=", results)

# Close the loop
loop.close()