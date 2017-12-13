
def line(d):
    print('+'+d*'----------+')

def gap(d):
    print('|'+d*'          |')

def windowWide(d):
    line(d)
    gap(d)
    gap(d)
    gap(d)
    gap(d)
    gap(d)


def window(w,h):
    for i in range(0,h):
        windowWide(w)
    line(w)
