"""What is Multiprocessing in Python?

Multiprocessing allows Python to run multiple processes simultaneously, each with its own memory space and own Python interpreter.

✔ It bypasses the GIL
✔ Best for CPU-bound tasks"""

from multiprocessing import Process
import time
def function(sec):
    print("starting process")
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    print(f"process done for {sec} seconds")
if __name__ == '__main__':
    p1 = Process(target=function, args=[2])
    p2 = Process(target=function, args=(10,)) #both way we can give arguments
 
    p1.start()
    p2.start()

    p1.join()
    p2.join()
# Both processes run in parallel, utilizing multiple CPU cores.
# if __name__ == "__main__" is mandatory on Windows



