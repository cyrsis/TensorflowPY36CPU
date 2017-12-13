from time import strftime

class PythonProjects():
    def __init__(self, msg):
        self.msg = msg
        self.print_message()
    
    def print_message(self):
        print(self.msg)

class Utilities(PythonProjects):
    def print_message(self):
        print(self.msg + ' @ ' + strftime("%Y-%m-%d"))

#===========================================
if __name__ == '__main__':
    msg = "A message"
    inst = PythonProjects(msg)  # Create an instance of this class
    util = Utilities(msg)       # Create an instance of this class 
