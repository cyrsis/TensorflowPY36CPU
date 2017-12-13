paragraph = '''djokovic will next head to Melbourne Park for the first
Grand Slam of the year at the Australian Open. he is looking forward to
reuniting with two other longtime rivals - Roger Federer and Rafael
Nadal. the Swiss and the Spaniard are returning to action after injuries
hampered their 2016 campaigns.'''



def fixCapitals(paragraph):
    paragraph = list(paragraph)
    paragraph[0] = paragraph[0].capitalize()
    paragraph.append(' ')
    paragraph.append(' ')

    for i in range(0,len(paragraph)):
        if paragraph[i] == '.':
            print(i)
            c = paragraph[i+2]
            c = c.capitalize()
            paragraph[i+2] = c
    paragraph = ''.join(paragraph)
    return paragraph
