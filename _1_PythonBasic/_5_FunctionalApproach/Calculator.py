OPERATORS = "+", "-", "*", "/"


def f_calculate(number1, operator, number2):
    return number1 + number2 if operator == "+" \
    else number1 - number2 if operator == "-" \
    else number1 * number2 if operator == "*" \
    else number1 / number2 if operator == "/" \
    else None


def f_get_number():
    return int(input("Enter an integer : "))


def f_get_operator():
    return input("Enter an Operator :")


def f_main():
    return f_calculate(
        f_get_number(),
        f_get_operator(),
        f_get_number(),

    )
     

if __name__ == '__main__':

    print("The result is %s " % f_main())
