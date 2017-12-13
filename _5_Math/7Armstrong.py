

def armTest(yourNum):
    length = len(str(yourNum))
    List = []
    total = 0
    for digit in str(yourNum):
            List.append(int(digit))
    for i in range(0,length):
        total = total + List[i]**length

    if total == yourNum:
        print(str(yourNum) + ' is ARMSTRONG')


for i in range(0,10000):
    armTest(i)

