import threading
import time

# 定义线程函数
def worker():
    print("Thread %s is running" % threading.current_thread().name)
    time.sleep(2)
    print("Thread %s is finished" % threading.current_thread().name)

# 创建线程
t1 = threading.Thread(target=worker, name="Thread-1")
t2 = threading.Thread(target=worker, name="Thread-2")

# 启动线程
t1.start()
t2.start()

# 等待线程执行完毕
t1.join()
t2.join()

print("All threads are finished")



import concurrent.futures
import time

# 定义任务函数
def task(name):
    print("Task %s is starting" % name)
    time.sleep(2)
    print("Task %s is finished" % name)

# 创建线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    tasks = []
    for i in range(5):
        t = executor.submit(task, i+1)
        tasks.append(t)

    # 等待任务执行完毕
    for t in concurrent.futures.as_completed(tasks):
        print("Task %s is done" % t.result())



import asyncio

# 定义协程函数
async def task(name):
    print("Task %s is starting" % name)
    await asyncio.sleep(2)
    print("Task %s is finished" % name)

# 创建事件循环对象
loop = asyncio.get_event_loop()

# 创建任务列表
tasks = [loop.create_task(task(i+1)) for i in range(5)]

# 执行任务
loop.run_until_complete(asyncio.wait(tasks))        