class PythonProjects():    
    def __init__(self, msg):
        self.msg = msg
        self.say_hello()
    
    def say_hello(self):
        for idx in range(10):
            print(str(idx)+ ' - ' + self.msg)

#====================================
if __name__ == '__main__':
    
    # Create an instance of the class
    inst = PythonProjects("hello")
