import asyncio

# 1. THE TASKS (The Orders)
async def slow_task():
    print("🐢 Slow Task: Started! (Need 2 seconds)")
    # 'await' tells the Event Loop: "I am waiting. Go do something else."
    await asyncio.sleep(2) 
    print("🐢 Slow Task: Finished!")

async def fast_task():
    print("🐇 Fast Task: Started! (Need 1 second)")
    await asyncio.sleep(1)
    print("🐇 Fast Task: Finished!")

# 2. THE MAIN ROUTINE
async def main():
    print("--- 🎡 Event Loop Starting ---")
    
    # We create the "Tickets" for the kitchen
    # gather() tells the loop: "Run these together."
    await asyncio.gather(slow_task(), fast_task())
    
    print("--- 🏁 Event Loop Closed ---")

# 3. START THE LOOP
# This creates the loop, runs main(), and closes the loop when done.
asyncio.run(main())