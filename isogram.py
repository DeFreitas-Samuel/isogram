def isogramCounter(fileName):
    counter = 0
    words = []
    isogramFile = open(fileName, "r")
    for lines in isogramFile:
        counter += 1

    isogramFile.close()
    return counter