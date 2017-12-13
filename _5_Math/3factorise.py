#ask for a number to factorise
print('what number do you want to factorise?')
# convert user input to integer
userNum = int(input())

for i in range(1,userNum+1):
#if remainder of userNum divided by loop variable is 0
    if userNum % i == 0:
#the present loop variable is a factor
#convert i (loop variable) to string before printing
        print(str(i) + ' is a factor')




