def main():
    print('This will print with "quote" in python')
    print('This will print with ""quote"" in python')
    print("This will print with \"quote\" in python")

    # Get to knw the index of the string
    stringIndex = "Victor"
    print(stringIndex[0])
    print(stringIndex[1])
    print(stringIndex[2])

    # Build in features for string

    print(stringIndex.upper())  # .Upper
    print(stringIndex.lower())  # .Lower
    print(len(stringIndex))  # .Length

    print(stringIndex + " " + str(12))  # ToString

    print(stringIndex.replace("Vic", "Ton"))  # Replace

    repeatString = "1abc2abc3abc4abc"

    print(repeatString.replace("abc", "ABC", 2))

    print("Normal String " + repeatString)
    print(" [1:6]        " + repeatString[1:6])
    print(" [1:6:2]      " + repeatString[1:6:2])
    print(" [::2]        " + repeatString[::2])  # alternate string
    print(" [::-2]        " + repeatString[::-2])  # alternate string
    print(" [0:3:1]       " + repeatString[0:3:1])  # Start from 0, Skips 3, Steps 2
    print(" 1::4            " + repeatString[1::4])

    print("This is first var (%s) and second var (%s)" % ('First', 'Second'))

    print("#" * 20)

    str1 = "Hello, World!"  # 定義字串
    print("讀取位置為2的元素 " + str1[5])  # 讀取位置為2的元素										#位置為2的元素是逗點’,’
    print("讀取位置從7到最後的子字串 " + str1[7:])  # 讀取位置從7到最後的子字串

    print("#" * 40)
    print("let's just do some line in here \n U see a line right?")

    print("#" * 40)
    print("This is a a tab \t tab \t tab ")

    print("#" * 40)
    print("""This will go many
     
     many 
     
     mnay line""")

    print("#" * 40)


    number2 = "1, 2, 3, 4, 5, 6"
    print(number2)
    print("This will take out the comma from the nunmbers "+ number2[0::3])


if __name__ == '__main__':
    main()
