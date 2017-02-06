def primeNumbers(start,end):
    "This function prints a list of n prime number"
    if start>end:
        return 101
    
    if start < 2:
        return 102 #"Prime numbers starts from 2"
    
    primes = []
    for i in range(start, end+1):
        if i==2:
            primes.append(2)
            continue # continue to the next i
        for j in range(2, i):
            if i % j == 0:break #break execution since we have found a factor
        else:
            primes.append(i)
    return primes
