import printClass
import pickle
man=[]
otherMan=[]
try:
    #file= open("file.txt")
    with open("file.txt") as file:
        '''
        output=open("out.txt", "w")
        print("Haist kotarache!", file= output)
        output.close()
        '''

        for i in file:
            try:
                (role, line_spoken) = i.split(":", 1)
                line_spoken=line_spoken.strip()
                if role== "Man":
                   man.append(line_spoken)
                elif role== "Other Man":
                    otherMan.append(line_spoken)
            except ValueError:
                pass
        #file.close()
except IOError as err:
    print('File error' + str(err))
    '''
    try:
    #manFile= open("man_file.txt", "a")
    with open("man_file.txt", "a") as manFile:
        printClass.print_file(man, fh=manFile)
    #otherManFile=open("other_man_file.txt","a")
    with open("other_man_file.txt","a") as otherManFile:
        printClass.print_file(otherMan, fh=otherManFile)
except IOError as err:
    print('File error'+str(err))

    '''
    '''
   finally:
    if 'manFile' and 'otherManFile' in locals():
        manFile.close()
        otherManFile.close() 
    '''
with open("mydata.pickle", 'wb') as savedata: #wb-whrite binary
    pickle.dump([1, 2, 'three'], savedata) #dump- to save data
with open("mydata.pickle", 'rb') as restoredata: #rb-read binary
    list= pickle.load(restoredata) #load- restotre data
print(list)
try:
    with open ("man_file.txt", 'wb') as manFile, open ("other_man_file.txt", 'wb') as otherManFile:
        pickle.dump(man, manFile)
        pickle.dump(otherMan, otherManFile)
except IOError as err:
    print('File error'+str(err))
except pickle.PickleError as perr:
    print("oppsss!"+str(perr))
try:
    with open('man_file.txt', 'rb') as manFile:
        rman= pickle.load(manFile)
except IOError as err:
    print('File error'+str(err))
except pickle.PickleError as perr:
    print("oppsss!"+str(perr))