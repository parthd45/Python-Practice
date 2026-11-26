import threading

def greet(name,age):
    print("Hello", name)
    print("Age", age)
t1 = threading.Thread(target=greet, args=("Aarav",10))
t1.start()
t1.join()