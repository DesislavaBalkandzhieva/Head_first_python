import pickle
from athleteList import AthleteList

def get_data(filename):
    print()
    #fff
def put_to_store(file_list):
    all_athletes={}
    for i in file_list:
        ath=get_data(i)
        all_athletes[ath.name]=ath
    try:
        with open('athlete.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as err:
        print('error :(')
    return (all_athletes)
def get_from_store():
    all_athletes={}
    try:
        with open('athlete.pickle', 'wb') as athf:
            pickle.load(all_athletes, athf)
    except IOError as err:
        print('error :(')
    return (all_athletes)