import time

primeList = []
primeList.append(1)
primeList.append(2)


def primeTest(testNum):
    prime = True
    for i in range(2,testNum,2):
        if testNum % i == 0:
            prime = False           
    return prime

def allPrimes(maxNum):
    for i in range(3,maxNum,2):
        if primeTest(i) == True:
            primeList.append(i)




print('What is your maximum number?')
maxNum = int(input())
print('These are all primes under ' + str(maxNum))
tic = time.clock()
allPrimes(maxNum)
toc = time.clock()
print('time taken in seconds: '+str(toc-tic))


