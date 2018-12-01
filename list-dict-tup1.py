def getEmailsFromFile(x):
    '''create a list of emails from the file'''
    newEmailList = []
    for i in x:
        if i.startswith("From"):
            h = i.split()
            for j in h:
                if "@" in j:
                    newEmailList.append(j)
        
    return newEmailList


def createDictOfEmails(y):
    '''create a dict of the emails from the file with key as email and value the 
    number of times a message as been sent from the given email'''
    dictEmails = {}
    for i in y:
        if i in dictEmails:
            dictEmails[i] += 1
        else:
            dictEmails[i] = 1
    return dictEmails


def createTupleAndGetCount(z):
    '''create a list of the tuples in the dict, sort them out in descending order
    and return the email with the highest count'''
    emailTuple = list(z.items())
    sortEmailTuple = sorted(emailTuple,key=lambda x:(-x[1],x[0]))
    return "{} {}".format(sortEmailTuple[0][0], sortEmailTuple[0][1])
    
    
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
emailList = openFile.read().splitlines()

#get emails from file
fileEmails = getEmailsFromFile(emailList)

#store emails in dict with their count
dictEmails = createDictOfEmails(fileEmails)

#create tuples and get answer
print(createTupleAndGetCount(dictEmails))