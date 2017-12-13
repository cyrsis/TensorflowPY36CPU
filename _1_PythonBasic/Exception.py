'''

Build in Exceptions - 
https://docs.python.org/3/library/exceptions.html

'''


def makeAnExceptionHandling():
    print("This will happen")
    try:
        print("Try something")
    except:
        print("Int the except block, this is not possible")
    else:
        print("This is execute other than first except")
    finally:
        print("This will happne no matter what")

makeAnExceptionHandling()
