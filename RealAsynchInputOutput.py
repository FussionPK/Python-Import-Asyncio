import asyncio

#define a coroutine that simulates a time consuming task
async def fetch_data(delay):
    print("Fetching data....")
    await asyncio.sleep(delay) #this is an input output operation with sleep
    print("Data Fetched >_< ")
    return {"data": "Some Data"} #return something


#define another coroutine that calls the first one above
async def main():
    print("start of main coroutine")
    task = fetch_data(2)
    #Await the fetch_data coroutine, pausing the execution of main until fetch_data completes
    result = await task
    print(f"Recieved Result: {result}")
    print("end of main coroutine")

#run the main coroutine
asyncio.run(main())