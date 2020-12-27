def isIsogram(word):
    charList = []
    for char in word:
        if char in charList:
            return False
        charList.append(char)
    return True
def isogramCounter(fileName):
    counter = 0
    listOfWords = []
    isogramFile = open(fileName, "r")
    for lines in isogramFile:
        cleanWord = lines.strip().lower()
        listOfWords.append(cleanWord)
    
    for word in listOfWords:
        if isIsogram(word) is True:
            counter += 1

    isogramFile.close()
    return counter