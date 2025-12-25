"""What is Multithreading in Python?

Multithreading allows a program to run multiple threads (tasks) concurrently within the same process.

📌 A thread is the smallest unit of execution.

🔹 Why Use Multithreading?

✔ To improve responsiveness
✔ To handle I/O-bound tasks efficiently
✔ To run tasks in parallel logically

❌ Not ideal for CPU-bound tasks in Python (because of GIL)

Thread Lifecycle

1️⃣ New
2️⃣ Runnable
3️⃣ Running
4️⃣ Blocked/Waiting
5️⃣ Dead

"""

import threading
import time
def function(seconds):
    print("Thread started")
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print("Thread finished")
t1=threading.Thread(target=function,args=[2])
t2=threading.Thread(target=function,args=(10,)) #both way we can give arguments
intit=time.time()
t1.start()
t2.start()
print(f"Time taken in multithreading: {time.time()-intit} seconds")
t1.join()
t2.join()
print(f"Time taken in multithreading: {time.time()-intit} seconds")