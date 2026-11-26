import threading

counter = 0
lock = threading.Lock()

def increase_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increase_counter)
t2 = threading.Thread(target=increase_counter)

t1.start()
t2.start()
t1.join()
t2.join()

print("Counter:", counter)