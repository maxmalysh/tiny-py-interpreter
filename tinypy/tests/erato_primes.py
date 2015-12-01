def sieve(upperlimit):
    # mark off all multiples of 2 so we can use 2*p as the step for the inner loop
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0
    # filter out non primes from the list, not really that important i could work with a list full of zeros as well
    return [x for x in l if x]