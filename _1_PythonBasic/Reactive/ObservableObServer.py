from rx import Observable,Observer

letters = Observable.from_(["Alpha","Beta","Gamma","Deleta","Epsilon"])

# With Class 's way of coding
class MySubscriver(Observer):
    def on_next(self, value):
        print(value)

    def on_completed(self):
        print("Completed")

    def on_error(self, error):
        print("Error occured :{0}".format(error))

# With Lambda and Cold Obserable on Subscribe 2 , since they will get the exact copy,. this is good and it is call cold observable

letters.subscribe(MySubscriver())
letters.subscribe(on_next = lambda value: print("Subscrive 2 Recieved " +value),
                  on_completed = lambda: print("Complete"),
                  on_error = lambda error:print("Error occour {0}".format(error))

                  )

letters.subscribe(on_next = lambda value: print("Short Recieved"+ value))

letters.map(lambda s: len(s)).filter(lambda i : i>5).subscribe(lambda value : print(value))






