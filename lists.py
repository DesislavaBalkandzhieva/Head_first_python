'''
#List
users=["Ivan","Petar","Raya"]
print(users[1])
print(users)
print(len(users))
users.append("Iva")
users.pop()
print(users)
users.extend(["Mila", "Georgi"])
print(users)
users.remove("Petar")
users.insert(1, "Katya")
print(users)


#List with different types
users2=["Ivan", 2002, "Katya", 1978, "Iva", 2005]
for i in users2:
    print(i)
count=0
while count<len(users2):
    print(users2[count])
    count=count+1

'''
users2 = ["Ivan", 2002, "Katya", 1978, "Iva", 2005,
        [28000, 8990, 8392]]
'''
print (users2 [0], [1], [0])
for i in users2:
    print(i)
isinstance(users, list)#chek if 'thing' is this type/ return True or False
len_users=len(users2)

for i in users2:
    if isinstance(i, list):
        for j in i:
            print (j)
    else:
        print(i)
print(isinstance(users2, list))
'''
arr = ["Ivan", 2002, "Katya", 1978, "Iva", 2005,
        ["hello", ["bye", 8392, "hi"]]]
for i in arr:
    if isinstance(i, list):
        for j in i:
            if isinstance(j, list):
                for k in j:
                    print(k)
            else:
                print (j)
    else:
        print(i)
#same but fast
def printArr(arr):
    for i in arr:
        if isinstance(i, list):
            printArr(i)
        else:
            print(i)
printArr(arr)