import string
Stringy = '''
Agnes: Why are you wearing your pajamas?
Vector: [sputters] These aren't pajamas! It's a warm-up suit.
Edith: What are you warming up for?
Vector: Stuff.
Margo: What sort of stuff?
Vector: Super-cool stuff you wouldn't understand.
Agnes: Like sleeping?
Vector: THEY ARE NOT PAJAMAS!
Me: Chicken is better with breadstuffs
'''

def removePunctuation(st):
    for c in string.punctuation:
        st = st.replace(c,'')

    return st

def lowerSplit(st):
    st = st.lower()
    st = st.split()
    return st 

def countWord(word,st):
    removePunctuation(st)
    lowerSplit(st)
    count = st.count(word)
    return print(word + ' repeats ' + str(count) + ' times')
    
    


    
