def primes(max):
    p, i = 0, 2
    while p != max:
        for x in range(2, i/2+1):
            if i % x == 0:
                break
        else:
            p += 1
            yield i
        i += 1

for x in primes(500):
    print x