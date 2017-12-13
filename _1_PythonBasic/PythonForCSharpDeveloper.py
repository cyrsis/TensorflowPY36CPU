# Python is
# Battery Included  -> Big Standard library, regular expression and web request
# Python 3 is highly OOP

#The folder in Python cannt import with a number as first digita
# _1_PythonBasic is the best I can do
import random


def get_days():

    # List<String> =  new list<String>();
    days = ['mon','tuse','wed','thurs','fri','sat','sun']

    return days


def get_random_reports():
    weather = ['sunny','lovely','cold']
    return weather[ random.randint(0,len(weather)) ]



def main():

    days = get_days()

    for day in days:
        report = get_random_reports()
        print("On {0} it will be {1}".format(days, report))


