def mysplit(strng):
    tmp = []
    tmpString = []
    chartmp = ""

    if strng.isspace():
        return tmp

    strng = strng.strip()

    if len(strng) == 0:
        return tmp

    if type(strng) == str:
        tmpStrng = strng + " "
        for char in tmpStrng:
            if char.isalpha() == True:
                chartmp += char

            elif char.isspace() == True:
                tmp.append(chartmp)
                chartmp = ""
    return tmp



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))