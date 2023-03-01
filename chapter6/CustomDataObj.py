class Athlete:
    def __init__(self, name, dob=None, times=[]):
        self.name=name
        self.dob=dob
        self.times=times

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])

def open_fies (filename):
    try:
        with open(filename) as file:
            data= file.readline()
            temp= (data.strip().split(","))
            return (Athlete(temp.pop(0), temp.pop(0), temp))
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

sarah=open_fies("sarah2.txt")
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
