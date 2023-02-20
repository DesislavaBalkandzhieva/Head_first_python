arr = ["Ivan", 2002, "Katya", 1978, "Iva", 2005,
        ["hello", ["bye", 8392, "hi"]]]

def printArr(arr):
    for i in arr:
        if isinstance(i, list):
            printArr(i)
        else:
            print(i)
print(arr)