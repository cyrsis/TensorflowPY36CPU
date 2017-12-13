def factorize(number):
    divisor=0
    divisors=[]
    for divisor in range(1,number+1):
        if number%divisor==0:
            divisors.append(divisor)
        divisor+=1
    return divisors

while True: # forever loop! 
    try:
        num = int(input("Please enter a number: "))
        print('{} {} {} {}'.format('the factors for',num,'are', factorize(num)))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        break
