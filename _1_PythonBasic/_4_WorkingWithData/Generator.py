# ========================================================================= #
#               Very large of collectioin of Data                           #
# :                                                                         #
# ========================================================================= #


#1,1,2,3,,5................
#Never ends

def fibon(n):
    a = b  =1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a +b
    return result


# print(fibobon(100)) #1000000 -> Will go a while

#how can we fix it?,


#

def fibon_g(n):
    a = b =1
    for i in range(n):
        yield a
        a,b = b, a+b


for x in fibon_g(100000000):
    print( x, x+1)
