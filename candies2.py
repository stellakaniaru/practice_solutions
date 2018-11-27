import itertools

def checkCandies(x):
    '''compares the packets to check if they can be equalized or not'''
    #loop through the keys in the dict
    for i in d:
        if i != '-1':
            #convert the key string into an int
            key = int(i)
            #convert the value string into a list
            value = d[i].split()
            #convert items in the list to int
            value2 = [int(x) for x in value]
            #get the total of all list elements
            sumValues = sum(value2)
            
            #check if the bags can be equalized. If no, return -1. If yes, return number of moves
            if sumValues % key != 0:
                print("-1")
            else:
                moves = 0
                avg = sumValues / key
                for i in value2:

                    if(i > avg):
                        moves = moves + (i - avg)
                print(int(moves))
                
def createListMap(y):
    '''creates a new list that has concatenated data spanning across multiple lines'''
    #iterates through list with file contents and concatenates data spanning across multiple lines
    data = " ".join(line.strip() for line in y if len(line)>=39)
    
    newCntList = []
    #loop through list with file content and append them to the new list.
    for i in y:
        #if the line does not span over multiple lines, add it as a single item to new list
        if len(i) <39:
            newCntList.append(i)
        #add the content that has already been filtered in data
        else:
            newCntList.append(data)
            break
    return newCntList
    


#read file contents
file = open("candy.txt", "r")

#store file contents in a list
rr = file.read().splitlines()

#take care of values that might span across multiple lines
contentList = createListMap(rr)

#create a dict where key is the number of packets and value is the contents of each packet
d = dict(itertools.zip_longest(*[iter(contentList)]*2, fillvalue=""))

#check if the bags can be equalized
checkCandies(d)
