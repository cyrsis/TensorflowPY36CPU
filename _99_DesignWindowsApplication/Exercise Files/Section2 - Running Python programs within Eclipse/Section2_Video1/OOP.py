
class PythonProjects():
    
    def __init__(self, msg):
        self.msg = msg
        self.say_hello()
    
    def say_hello(self):
        print(self.msg)


#====================================
if __name__ == '__main__':
    print('hi')

    # Create an instance of the class
    inst = PythonProjects("Initial message")
