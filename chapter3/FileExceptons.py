import os.path

#if os.path.exists("file.txt"):
try:
    file= open("file.txt")
    for i in file:
        #print(file.readline(), end=" ")
        # i.find(":")
        #if not i.find(":")==-1:
        try:
            (role, line_spoken) = i.split(":", 1)
            print(role, end=" ")
            print(" said: ", end=" ")
            print(line_spoken, end=" ")
        except ValueError:
            pass
    file.close()
except IOError:
    print("the file is missing!")

