from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")

class PythonProjects():
    def __init__(self, msg):
        self.msg = msg
        self.print_message()
        # Create an instance of the class  
        util = Utilities()      
        util.print_msg_with_time(msg)
    
    def print_message(self):
        print(self.msg)


class Utilities():
    def print_msg_with_time(self, msg):
        print(msg + ' @ ' + today)

#===========================================
if __name__ == '__main__':
    # Create an instance of the class
    inst = PythonProjects("A message")

