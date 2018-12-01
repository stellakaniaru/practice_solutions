def getTimeFromFile(x):
    '''create a list of time from the file'''
    newTimeList = []
    for i in x:
        if i.startswith("From"):
            h = i.split()
            for j in h:
                if ":" in j:
                    newTimeList.append(j.split(":"))
        
    return newTimeList

def createDictOfTime(y):
    '''create a dict of the time from the file with key as hour and value the 
    count of the hour'''
    dictEmails = {}
    for i in y:
        if i[0] in dictEmails:
            dictEmails[i[0]] += 1
        else:
            dictEmails[i[0]] = 1
    return dictEmails


def createTupleAndGetCount(z):
    '''create a list of the tuples in the dict, sort them out in descending order
    and print out hour and count for each item'''
    hourTuple = list(z.items())
    sortHourTuple = sorted(hourTuple,key=lambda x:(int(x[0]),-x[1]))
    for i in sortHourTuple:
         print("{} {}".format(i[0], i[1]))
            
           
#specify name of file
file = "mbox-short.txt"

#get file name from user
fileName = input("Enter a file name:")
while True:
    if fileName == file:
        break
    else:
        fileName = input("Open failed, TRY AGAIN:")
    
#open file contents and store in list
openFile = open(fileName, "r")
TimeList = openFile.read().splitlines()

#get emails from file
fileTime = getTimeFromFile(TimeList)

print(fileTime)

#store emails in dict with their count
dictTime = createDictOfTime(fileTime)

print(dictTime)

#create tuples and get answer
createTupleAndGetCount(dictTime)