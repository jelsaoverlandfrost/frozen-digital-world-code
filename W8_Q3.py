import time


class StopWatch(object):
    def __init__(self, start_time=time.time(), end_time=-1):
        self.start_time = start_time
        self.end_time = end_time

    def start(self):
        self.start_time = time.time()
        self.end_time = -1

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.end_time == -1:
            return None
        else:
            finalans = (self.end_time - self.start_time) * 1000
            return round(finalans, 1)


sw = StopWatch()
time.sleep(10)
sw.stop()
print sw.elapsed_time()
sw.start()
time.sleep(0.2)
print sw.elapsed_time()
sw.stop()
print sw.elapsed_time()
