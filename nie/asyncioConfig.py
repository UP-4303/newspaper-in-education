import asyncio
import traceback

# Not sure if the loop part works
def loopExceptionHandler(loop, context):
    print("Asyncio Exception:", context.get("exception", context["message"]))

def asyncioSetup():
    loop = asyncio.get_running_loop()
    loop.set_exception_handler(loopExceptionHandler)

def exceptionHandler(task, coro):
    try:
        task.result()
    except Exception as e:
        print(f"Exception in task {coro.__name__}:", e)
        traceback.print_exception(type(e), e, e.__traceback__)

def createTask(coro, name=None):
    task = asyncio.create_task(coro, name=name)
    task.add_done_callback(lambda t: exceptionHandler(t, coro))
    return task

# Task utils
def allTasks():
    return asyncio.all_tasks()

def taskKiller():
    [task.cancel() for task in allTasks()]