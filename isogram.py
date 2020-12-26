def isAnagram(word):
     
    charList = []
    for char in word:
        if char in charList:
            return False
        charList.append(char)
    return True

def isogramCounter(fileName):
    wordList = []
    counter = 0
    isogramText = open(fileName, "r")
    for lines in isogramText:
        cleanLines = lines.strip().lower()
        wordList.append(cleanLines)
    for words in wordList:
        if isAnagram(words) is True:
            counter +=1


    isogramText.close()
    return counter