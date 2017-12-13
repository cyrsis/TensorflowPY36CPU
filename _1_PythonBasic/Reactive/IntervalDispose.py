from rx import *
import time

disposable= Observable.interval(1000).map(lambda i:"{0} Mississippi".format(i)).subscribe(lambda s: print(s))

time.sleep(5)

print("Unsubscribing")
disposable.dispose()


time.sleep(5)