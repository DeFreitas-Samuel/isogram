def isogramCounter(fileName):
    counter = 0
    isogramFile = open(fileName, "r")
    for lines in isogramFile:
        counter +=1

    return counter