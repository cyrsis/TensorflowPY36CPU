

primeList = []
primeList.append(1)


def factorCount(testNum):
    factors = 0
    for i in range(1,testNum+1):
        if testNum % i == 0:
            factors = factors + 1
    return factors

def allPrimes(maxNum):
    for i in range(1,maxNum):
        if factorCount(i) == 2:
            primeList.append(i)
    print(primeList)


print('What is your maximum number?')
maxNum = int(input())
print('These are all primes under ' + str(maxNum))
allPrimes(maxNum)



