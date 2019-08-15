import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(3)]

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    
    exitmutexes[myId].acquire()
    for mutex in exitmutexes:
        print(mutex.locked())

for i in range(3):
    thread.start_new_thread(counter, (i, 10))

for mutex in exitmutexes:
    while not mutex.locked(): pass

for mutex in exitmutexes:
    print(mutex.locked())

for mutex in exitmutexes:
    mutex.release()

for mutex in exitmutexes:
    print(mutex.locked())


print('Main thread exiting!')

