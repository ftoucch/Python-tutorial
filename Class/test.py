import asyncio

# Making the name function async
async def name():
    # Simulating an async operation, e.g., fetching data from a server
    await asyncio.sleep(5)  # Simulate a delay
    return 'Hello world'


async def print_hello():
    # Now you can await the async name() function
    results = await name()
    return results

# Using asyncio.run to execute the async code
hello = asyncio.run(print_hello())

print(hello)

print('My name is khan')
