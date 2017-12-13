# Example of adding a text encoding to existing file-like object

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

print(text)


rawtext = urllib.request.urlopen('http://www.yahoo.com')
displaytext = io.TextIOWrapper(rawtext,encoding='utf-8')
outputText = displaytext.read()

print(outputText)
