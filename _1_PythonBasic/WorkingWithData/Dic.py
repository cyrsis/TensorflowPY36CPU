#victor 
#20/12/2017 
#Created @ 2017-12-20 01:36

char_count = {'a':5,'b':7,'A':5,'t':8,'B':10}

char_frequency = dict()

for key, value in char_count.items():
    if key.lower() in char_frequency:
        char_frequency[key.lower()] += value
    else:
        char_frequency[key.lower()] = value

print(char_frequency)
