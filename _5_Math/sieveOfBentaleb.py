import time

print('Enter a number to print all primes less or equal it')
num = int(input())
startTime = time.clock()
isPrime = [True] * (num + 1)
isPrime[0] = False
isPrime[1] = False
print('These are the primes <= ' + str(num))
primeList = []
for i in range(2, num + 1):
    if isPrime[i]:
        primeList.append(i)
        # AT THIS POINT EVERY NUMBER IS PRIME UNLESS
        # IT HAS BEEN REMOVED BECAUSE ITS A MULTIPLE OF ANOTHER PRIME
        for j in range(i * 2, num + 1, i):
            isPrime[j] = False
endTime = time.clock()
print(primeList)
print('It took : ' + str(endTime - startTime))
