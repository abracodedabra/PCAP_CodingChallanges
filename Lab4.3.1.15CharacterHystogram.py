import random
from os import strerror
from random import randrange


userInput = input("Enter Filename: ")
userInputEnding = userInput + '.txt'
countDic = {}
dicSorted = {}


try:
    sampleInput = open(userInputEnding, 'wt')
    for line in range(3):
        sampleInput.write(" ")
        for i in range(3):
            tmp = random.randint(97, 105)
            sampleInput.write(chr(tmp))
            if chr(tmp) not in countDic:
                countDic[chr(tmp)] = 1
            else:
                countDic[chr(tmp)] += 1

    sampleInput.close()
except IOError:
    print("File exist or filename not correct")

try:
    textausgabe = open(userInputEnding, 'rt')
    for ch in textausgabe:
        print(ch)
    textausgabe.close()

except IOError:
    print("File couldn't be opened")

print(countDic)
for key in countDic:
    print(key, "-->", countDic[key])
print()

try:
    userInputToHist = userInput + '.hist'
    newfile = open(userInputToHist, 'w')
    for char in sorted(countDic.keys(), key=lambda x: countDic[x], reverse=True):
        print(char, "-->", countDic[char])
        newfile.writelines(char + " --> " + str(countDic[char]) + " | ")
    newfile.close()
except IOError:
    print("write Histo-File unsuccesfull")