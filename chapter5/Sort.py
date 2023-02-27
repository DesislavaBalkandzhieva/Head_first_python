def open_fies (filename):
    try:
        with open(filename) as file:
            data= file.readline()
            return (data.strip().split(","))
    except IOError as e:
        print("IOERROR")
        return (None)
'''
with open ("james.txt") as jamesFile:
    lineja=jamesFile.readline()
james=lineja.strip().split(",")
with open("julie.txt") as julieFile:
    lineju=julieFile.readline()
julie=lineju.strip().split(",")
with open("mikey.txt") as mikeyFile:
    linem=mikeyFile.readline()
mikey=linem.strip().split(",")
with open("sarah.txt") as sarahFile:
    lines=sarahFile.readline()
sarah=lines.strip().split(",")
'''
james=open_fies("james.txt")
julie=open_fies("julie.txt")
mikey=open_fies("mikey.txt")
sarah=open_fies("sarah.txt")
'''
print(james)
print(julie)
print(mikey)
print(sarah)
print("sort:")
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
'''

def sanitize (time):
    if '-' in time:
        splitter='-'
    elif ':' in time:
        splitter=':'
    else:
        return (time)
    (mins, secs)= time.split(splitter)
    return (mins+'.'+secs)

'''
jamesarr=[]
juliearr=[]
mikeyarr=[]
saraharr=[]
for i in james:
    jamesarr.append(sanitize(i))
for i in julie:
    juliearr.append(sanitize(i))
for i in mikey:
    mikeyarr.append(sanitize(i))
for i in sarah:
    saraharr.append(sanitize(i))
'''

print("SORT II")
james=sorted([sanitize(t) for t in james])
print(james)
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))


unique_james=[]

for i in james:
 if (i not in unique_james):
     unique_james.append(i)
print(unique_james[0:3])

#print(sorted(set(james)[0:3]))


