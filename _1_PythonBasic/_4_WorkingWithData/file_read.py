# loream_file = open("lorem.txt","r")
#
# for line in loream_file:
#     print(line)
#
#
# loream_file.close()


with open("lorem.txt") as loream_file:
    loream_file.read()
    print(loream_file.tell())

