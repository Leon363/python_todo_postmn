from threading import Thread

def worker():
    print("worker started")
    print("worker finished")

thread1 = Thread(target=worker)
thread2 = Thread(target=worker)

thread1.start()
thread2.start()

print("Main thread working")

