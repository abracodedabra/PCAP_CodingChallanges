numbers = [[" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"],
           ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"],
           ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"],
           ["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], [" ", " ", "#"],
           ["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"],
           ["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"],
           ["#", "#", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"],
           ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"],
           ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"],
           ["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"]]

indexDic = {"0": 45, "1": 0, "2": 5, "3": 10, "4": 15, "5": 20, "6": 25, "7": 30, "8": 35, "9": 40}

def inputChange():
    userInput = input("Bitte geben Sie eine oder mehrere Zahlen zwischen 0 und 9 ein: ")
    indexNmr = []
    for i in range(len(userInput)):
        indexNmr.append(userInput[i])

    return indexNmr


def printNumber(indexNmr):
    for item in indexNmr:
        tmp = indexDic[item]

        for i in range(1):
            for y in range(3):
                print(numbers[tmp][y], end="")
            print(" ", end="")
    print()
    for item in indexNmr:
        tmp2 = indexDic[item] + 1
        for i in range(1):
            for y in range(3):
                print(numbers[tmp2][y], end="")
            print(" ", end="")
    print()
    for item in indexNmr:
        tmp2 = indexDic[item] + 2
        for i in range(1):
            for y in range(3):
                print(numbers[tmp2][y], end="")
            print(" ", end="")
    print()
    for item in indexNmr:
        tmp2 = indexDic[item] + 3
        for i in range(1):
            for y in range(3):
                print(numbers[tmp2][y], end="")
            print(" ", end="")
    print()
    for item in indexNmr:
        tmp2 = indexDic[item] + 4
        for i in range(1):
            for y in range(3):
                print(numbers[tmp2][y], end="")
            print(" ", end="")
    print()





printNumber(inputChange())
