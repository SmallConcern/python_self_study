
def _sqrrt(n, lower, upper, error):
    mid = (lower + upper) / float(2)
    while abs(mid**2 - n) > error*float(2):
        mid = (lower + upper) / float(2)
        if mid**2 < n:
            lower = mid
        else:
            upper = mid
    return mid

def sqrt(n, error):
    lower = n/float(n)
    upper = (n+lower)/float(2)
    return _sqrrt(n, lower, upper, error)


import math
n = 12345556
print "{} {}".format(sqrt(n, 0.0001), math.sqrt(n))