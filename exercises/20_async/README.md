# 20 Async Python & the Event Loop

### The Mental Model: One Chef, Many Pots
In synchronous Python, waiting for I/O (a database query or an LLM API call) blocks the entire operating system thread.
In asynchronous Python:
- The **Event Loop** is a single chef in a kitchen.
- When an operation waits for network I/O (`await asyncio.sleep()` or `await client.post()`), the chef steps away to tend another pot.
- When the network response arrives, the chef resumes the coroutine where it left off.
- **Never run blocking CPU loops inside async functions** without `asyncio.to_thread()`, or you will freeze the entire event loop!
