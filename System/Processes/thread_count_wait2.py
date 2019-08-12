import _thread as thread

stdoutmutex = thread.allocate_lock()

exitmutexes = [False] * 3

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()

    exitmutexes[myId] = True

for i in range(3):
    thread.start_new_thread(counter, (i, 10))

while False in exitmutexes: pass

print('Main thread exiting!')
