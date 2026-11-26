import threading
import time
def greet1():
    time.sleep(3)
    print("Hello from the thread 1")
def greet2():
    print("Hello from the thread 2")
def greet3():
    print("Hello from the thread 3")    
t1 = threading.Thread(target=greet1)
t2 = threading.Thread(target=greet2)
t3 = threading.Thread(target=greet3)
t1.start()
t1.join()
t2.start()
t3.start()
print("Main Program Ended")