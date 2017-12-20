current_speaker = None


def register(name):
    global current_speaker  # Global varable is pretty bad #Global
    current_speaker = name


def speak(text):
    print("[%s] %s" % (current_speaker, text))



def f_speak(text, speaker=None):
    print("[%s] %s" % (speaker, text))

    
class Speaker(): # OOP Approach

    def __init__(self, name):
        self._name = name

    def speak(self, text):
        print("[%s] %s" % (self._name, text))


if __name__ == '__main__':
    register("Victor")
    speak("Hello world")
    register("Tommy")
    speak("Some crab")


    victor = Speaker("Victor2")
    victor.speak("Hello world")
    mary= Speaker("Mary")
    mary.speak("I am Mary")

    f_speak("Hello there from Function","Victor")
    f_speak(speaker="Victor",text="This may work")

