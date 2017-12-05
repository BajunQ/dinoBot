import csv


def csvSearch(group):
    groupList = []
    val = 0
    ready = 0
    with open('class.csv', "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == group:
                groupList.append([row[1], row[2]])
                val+=1
                ready = 1
    if ready:
        print(groupList)
        return groupList
    else: return 0


def showAll(): 
    groupList = []
    with open('groups.csv', "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            groupList.append(row[0])
    return groupList
    

        
