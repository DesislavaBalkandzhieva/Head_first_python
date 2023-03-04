

def open_fies (filename):
    try:
        with open(filename) as file:
            data= file.readline()
            temp= (data.strip().split(","))
            return (AthleteList(temp.pop(0), temp.pop(0), temp))
    except IOError as e:
        print("IOERROR")
        return (None)



def sanitize (time):
    if '-' in time:
        splitter='-'
    elif ':' in time:
        splitter=':'
    else:
        return (time)
    (mins, secs)= time.split(splitter)
    return (mins+'.'+secs)
#built in list class
class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name=name
        self.dob=dob
        self.extend(times)
    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])


james= open_fies("james2.txt")
print(james.name+str(james.top3()))
julie= open_fies("julie2.txt")
print(julie.name+str(julie.top3()))
mikey= open_fies("mikey2.txt")
print(mikey.name+str(mikey.top3()))
sarah= open_fies("sarah2.txt")
print(sarah.name+str(sarah.top3()))



vera=AthleteList('Vera Vi')
print(vera.name)
vera.append('1.23')
vera.extend(['2.33','4.01', '3.24'])
print(vera.top3())