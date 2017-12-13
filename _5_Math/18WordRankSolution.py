import string
text = open('HarryPotterCh1.txt','r')
text = text.read()
words = []
dictionary = {}

def removePunctuation(st):
    for c in string.punctuation:
        st = st.replace(c,'')
    return st

def lowerSplit(st):
    st = st.lower()
    st = st.split()
    return st

def countWord(word, st):
    count = 0
    count = st.count(word.lower())
    return count

def nonRepeat(wordList):
    for i in range(0,len(wordList)):
        if wordList[i] not in words:
            words.append(wordList[i])
    return words

text = removePunctuation(text)
text = lowerSplit(text)
words = nonRepeat(text)

for x in range(0,len(words)):
    keyword = words[x]
    dictionary[keyword] = countWord(keyword,text)

rankedList = sorted(dictionary, key=dictionary.get, reverse = True)

for i in range(0,len(words)):
    word = rankedList[i]
    print(word + ' repeats '+ str(dictionary[word])+ ' times')
