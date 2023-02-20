
def printArr(arr, indent= False, level=0):
        for i in arr:
            if isinstance(i, list):
                printArr(i, indent, level+1)
            else:
                if indent:
                    for i in range(level):
                        print("\t", end=" ")
                print(i)
