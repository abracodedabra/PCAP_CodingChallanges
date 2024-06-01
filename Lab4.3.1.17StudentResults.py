from os import strerror

klassenliste = {}

try:
    listInput = open('Jekylls_file.txt', 'wt')
    global name
    global note
    for i in range(5):
        name = input("name eingeben: ")
        note = int(input("note eingeben: "))
        listInput.writelines(name + " " + str(note) + '\n')
        if name not in klassenliste:
            klassenliste[name] = note
        else:
            klassenliste[name] += note
    listInput.close()
except:
    print("einfaches Except")


print(klassenliste)
