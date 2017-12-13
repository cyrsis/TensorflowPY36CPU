# More speedy and less memory foot print for coroutine
# Only search of keyword "Coroutine" would show up
import pdb


def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('coroutine')
next(search)
# output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("Don't you love me?")
search.send("Don't you love me?")
search.send("I love coroutine instead!")
search.send("I love coroutine instead!")
search.send("I love coroutine instead!")


# output: I love coroutine instead!

def searchfor(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search2 = searchfor('Tony')
next(search2)

pdb.set_trace()  # c , w , a ,s,n
search2.send("Are u really Tony")
search2.send("U are Victor")

search2.close()