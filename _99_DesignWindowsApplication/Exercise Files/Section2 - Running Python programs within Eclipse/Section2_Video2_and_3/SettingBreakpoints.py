
class PythonProjects():
    def __init__(self, msg):
        self.msg = msg
        self.print_message()
    
    def print_message(self):
        print(self.msg)


#===========================================
if __name__ == '__main__':
    # Create an instance of the class
    inst = PythonProjects("A message")

