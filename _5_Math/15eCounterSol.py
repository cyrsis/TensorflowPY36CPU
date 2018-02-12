Stringy = 'This here is a very nice English sentence'


def eCounter(st):
    count = 0
    for c in st.lower():
        if c == 'e':
            count = count + 1
    print('There are ' + str(count) + ' e\'s in this sentence')
