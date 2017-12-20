def p_grade_description(gp):
    if gp >7:
        return "Good"
    if gp>5:
        return "sufficient"

    return "insufficient"


if __name__ == '__main__':
    print(p_grade_description(8))
    print(lambda gp : "good" if gp>7 else "sufficient" if gp>5 else "insufficient",(8))
