

def eingaben():
    regTxt = "Bitte geben Sie eine Shift-Zahl zw. 1 und 25 ein: "
    errorTxt = "Das war ein ungueltiger Wert! Bitte Wert zw. 1 und 25 eingeben: "

    def texteingabe():
        global unencrpdTxt
        unencrpdTxt = input("Bitte Nachricht zur Verschlüsselung eingeben: ")
        return unencrpdTxt

    def sveingabe(regTxt):
        global shiftValue
        shiftValue = int(input(regTxt))
        if shiftValue < 1 or shiftValue > 25:
            sveingabe(errorTxt)
        return shiftValue

    texteingabe()
    sveingabe(regTxt)
    return unencrpdTxt, shiftValue


def encryptTxt(unencrpdTxt, shiftValue):
    global encrpdTxt
    encrpdTxt = ""
    shiftencTxt = ""
    isUP = bool
    isLow = bool

    for char in unencrpdTxt:
        if not char.isalpha():
            continue
        else:
            if char.isupper():
                isUP == True
            elif char.islower():
                isLow == True

            shift = ord(char) + shiftValue
            print("shift", shift)
            if isUP and shift > ord("Z"):
                diff = shift - ord("Z")
                shift = ord("A") + diff
                isUP = False
            elif isLow and shift > ord("z"):
                diff = shift - ord("z")
                shift = ord("a") + diff
                isLow = False



            #print(char, char.isupper(), char.islower())
                encrpdTxt += chr(shift)
    print(encrpdTxt)



    '''for char in encrpdTxt:
        tmp = ord(char)
        print(tmp)
        if char.isupper():
            tmp = ord(char)
            if char > ord("Z"):
                diff = tmp - ord("Z")
                shift = ord("A") + diff
                shiftencTxt += chr(shift)
            else:
                shiftencTxt += char
        elif char.islower():
            print("islow / tmp:", tmp)
            if tmp > ord("z"):
                diff = tmp - ord("z")
                shift = ord("a") + diff
                shiftencTxt += chr(shift)
            else:
                shiftencTxt += char
        else:
            print("geht nich")'''



    print(shiftencTxt)

eingaben()
encryptTxt(unencrpdTxt, shiftValue)