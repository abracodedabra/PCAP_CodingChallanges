import os

pfad = input("Bitte path eingeben: ")
directory = input("Bitte dir eingeben: ")

def find(path, dir):
    os.chdir(path)
    print(os.getcwd())
    for pfad in os.listdir("."):
        if pfad == dir:
            print(os.getcwd() + " " + pfad)


    '''os.chdir(path)
    print(os.listdir(dir))'''

try:
    os.makedirs("tree\\c\\otherCourses\\cpp")
    os.makedirs("tree\\c\\otherCourses\\python")
    os.makedirs("tree\\cpp\\otherCourses\\c")
    os.makedirs("tree\\cpp\\otherCourses\\python")
    os.makedirs("tree\\python\\otherCourses\\c")
    os.makedirs("tree\\python\\otherCourses\\cpp")
except:
    find(pfad, directory)


