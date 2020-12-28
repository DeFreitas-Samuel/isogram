def isIsogram(word):
    newWord = word.strip().lower()
    charlist = []
    for char in newWord:
        if char in charlist:
            return False
        charlist.append(char)
    return True

def isogramCounter(fileName):
    counter = 0
    isogramFile = open(fileName, "r")
    for lines in isogramFile:
        if isIsogram(lines) is True:
            counter += 1
    isogramFile.close()
    return counter

isIsogram("Asa")