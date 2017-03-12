import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

def _ways_to_step_helper(step_opts, num_steps, memo):
    if num_steps in memo: return memo[num_steps]
    if num_steps == 0: return 1
    elif num_steps < 0: return 0
    ways = 0
    for step in step_opts:
        ways += _ways_to_step_helper(step_opts, num_steps - step, memo)
    memo[num_steps] = ways
    return ways

@timeit
def ways_to_step(step_opts, num_steps):
    memo = {}
    return _ways_to_step_helper(step_opts, num_steps, memo)

@timeit
def dp_ways_to_step(steps):
    if steps < 0: return 0
    if steps <= 1: return 1
    paths = [1, 1, 2]
    for x in range(3, steps+1):
        count = paths[2] + paths[1] + paths[0]
        paths[0] = paths[1]
        paths[1] = paths[2]
        paths[2] = count
    return paths[2]


class TestWaysToStep(object):
    def test_ways_to_step(self):
        print ways_to_step([1,2,3], 100)
        print dp_ways_to_step(100)