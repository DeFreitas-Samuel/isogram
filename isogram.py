def isogramCounter(fileName):
    counter = 0
    isogramText = open(fileName, "r")
    for lines in isogramText:
        counter += 1

    return counter