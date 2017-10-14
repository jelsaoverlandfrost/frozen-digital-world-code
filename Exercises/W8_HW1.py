class Time(object):
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_elapsed_time(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds

    def set_elapsed_time(self, seconds):
        if seconds >= 86400:
            seconds %= 86400
        self._hours = seconds / 3600
        self._minutes = (seconds % 3600) / 60
        self._seconds = seconds - 3600 * self._hours - 60 * self._minutes

    def __str__(self):
        return 'Time: %2d:%2d:%2d' % (self._hours, self._minutes, self._seconds)

    elapsed_time = property(get_elapsed_time, set_elapsed_time)


t = Time(10, 19, 10)
print t.elapsed_time
t.elapsed_time = 555550
print t.elapsed_time
print t