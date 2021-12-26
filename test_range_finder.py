import range_finder
import time
import timeit

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print ('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result

    return timed

@timeit
def get_ranging_timer():
    range = range_finder.get_range()

while True:
    get_ranging_timer()