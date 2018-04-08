import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadId =  thread_id
        self.name = name
        self.counter = counter

    def run(self):

        print "Stating " + self.name
        thread_lock.acquire()
        print_time(self.name, 5, self.counter)
        thread_lock.release()
        print "Exiting " + self.name


def print_time(thread_name, counter, delay):
        while counter:
            if exitFlag:
                thread_name.exit()
            time.sleep(delay)
            print "%s: %s" % (thread_name, time.ctime(time.time()))
            counter -= 1

thread_lock = threading.Lock()
threads = []
thread_1 = myThread(1,"Thread-1",1)
thread_2 = myThread(2,"Thread-2",2)



thread_1.start()
thread_2.start()

print "Exiting Main Thread"
