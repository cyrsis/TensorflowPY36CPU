from rx import *

numbers = Observable.range(1,10)

numbers.subscribe(lambda value: print(value))

greeting = Observable.just("Hello Word!")
greeting.subscribe(lambda value: print(value))


