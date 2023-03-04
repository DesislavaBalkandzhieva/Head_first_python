'''
class Athlete:
    def __init__(self, name, dob=None, times=[]):
        self.name=name
        self.dob=dob
        self.times=times

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time (self, time):
        self.times.append(time)

    def add_times (self, list_times):
        self.times.append(list_times)

'''

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

#sarah=open_fies("sarah2.txt")
'''
(sarah_name, sarah_dob)= sarah.pop(0), sarah.pop(0)
print(sarah_name+ str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
'''
'''
sarah_data={}
sarah_data['name']=sarah.pop(0)
sarah_data['dob']=sarah.pop(0)
sarah_data['time']=sarah
print(sarah_data['name']+ str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
'''
james= open_fies("james2.txt")
print(james.name+str(james.top3()))

vera=AthleteList('Vera Vi')
vera.append('1.23')
vera.extend(['2.33','4.01', '3.24'])
print(vera.top3())