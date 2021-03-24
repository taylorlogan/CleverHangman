'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Logan Green    ltg6
'''

import random


def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    
    print("How many misses do you want? Hard has 8 and Easy has 12.")
    easyOrHard = input("(h)ard or (e)asy> ")
    numOfMisses = 0
    if easyOrHard == 'h':
        numOfMisses = 8
    else:
        numOfMisses = 12
    
    return numOfMisses 


def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''

    hangmanWord2 = ""

    for char in hangmanWord:
        hangmanWord2 += (char + " ")   
    
    guessed = ''
    hang = ''
    
    alpha = 'abcdefghiijklmnopqrstuvwxyz'
#     for char in lettersGuessed:
#             alpha = alpha.replace(char, ' ')
    for let in alpha:
        if let not in lettersGuessed:
            guessed += let
        elif let in lettersGuessed:
            guessed += ' '
    
    for i in hangmanWord:
        hang += i + ' '
#     displayString = hangmanWord2
#     guess = handleUserInputLetterGuess(lettersGuessed, displayString)
#     if guess in alpha:
#         alpha = alpha.replace(guess, ' ')
    
            
    str1 = "letters not yet guessed: " + guessed
    str2 = "misses remaining = " + str(missesLeft)
    str3 = hang
    
    
    return str1 + "\n" + str2 + "\n" + str3


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    
    print(displayString)
    letter = input("letter> ")
    
    while letter in lettersGuessed:
        print("you already guessed that")
        letter = input("letter> ")
    return letter


def handleUserInputDebugMode():
    '''
    this function prompts the user on whether or not they would
    like to play the game's DEBUG mode ('d' corresponds to yes,
    'p' to no) and returns True or False based on the answer
    '''
    gameplayType = input("Which mode do you want: (d)ebug or (p)lay: ")
    
    DEBUG = False
    if gameplayType == 'd':
        DEBUG = True
    else:
        DEBUG = False
    
    return DEBUG


def handleUserInputWordLength():
    '''
    this function prompts the user on how many letters long they would
    like the word they guess to be
    '''
    wordLen = input("How many letters in the word you'll guess: ")
        
    return int(wordLen)
    
    
def createTemplate(currTemplate, letterGuess, word):
    '''
    this function creates the word template that the user will
    see in order to make more guesses on what the secret word is
    '''
#     secretWord = []
#     letidx = []
#     for let in word:
#             secretWord.append(let)
#       
#     for num in range(len(secretWord)):
#         if secretWord[num] == letterGuess:
#             letidx.append(num)
#     
#     currTemplate = list(currTemplate)
#     
#     for num in letidx:
#         currTemplate[num] = letterGuess
#         
#     currTemplate = ''.join(currTemplate)
#         
#     return currTemplate

    currTemplate = list(currTemplate)
    for i in range(len(word)):
        if word[i] == letterGuess:
            currTemplate[i] = letterGuess
    
    ret = ''
    
    for i in currTemplate:
        ret += i
        
    return ret


def getNewWordList(currTemplate, letterGuess, wordList, DEBUG):
    '''
    this function creates a template for every word in wordList and
    returns the key-value pairs corresponding to the templates in
    descending order
    '''
    dict = {}
    d2 = {}
    num = 1
    for word in wordList:
        temp = createTemplate(currTemplate, letterGuess, word)
#         print(temp)
#         if temp not in dict:
#             num = 1
#             dict.update({temp:num})
#             d2.update({temp:[word]})
#         else:
#             num += 1
#             dict[temp] = num 
#             d2[temp].append(word)
        if temp not in dict.keys():
            dict[temp] = []
        dict[temp].append(word)

    #dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)
    #print(dict)
    final = []
#     for k,v in dict:
#         print(str(k) + " : " + str(v))
    
    #ordered = sorted(dict.items(), key = lambda kv: (kv[1],kv[0]), reverse = True)
    #print(ordered)
    #print(sorted(dict.items(), key = lambda kv: (kv[1],kv[0]), reverse = True))
    
    for k,v in dict.items():
        final.append(str(k) + " : " + str(v) + '\n')

#     for k,v in ordered:
#         final.append(str(k) + " : " + str(v) + '\n')
     
    #print(final)
    final = ''.join(final)
    
    #final = sorted(final, key = lambda x:x[0])

#     max = 0
#     tup = ()
#     for item in dict.items():
#         if int(item[1]) > max:
#             max = item[1]
#             tup = item[0]
#             
    max2 = 0
    lst2 = []
    #bestOne = ()
    for pair in dict.items():
        if len(pair[1]) > max2:
            max2 = len(pair[1])
            bestOne = pair
        elif len(pair[1]) == max2:
            if pair[0].count('_') > bestOne[0].count('_'):
                bestOne = pair
        lst2.append(pair)
  
    lst2 = sorted(lst2, key = lambda x:x[0])
    #print(lst2)

#     print(max)
#     print(tup)
#     print(final)
    
    if DEBUG:
        for i in range(len(lst2)):
            print(lst2[i][0] + ' : ' + str(len(lst2[i][1])))
        print('# keys = ' + str(len(dict)))
    

    return bestOne


def processUserGuessClever(guessedLetter, hangmanWord, missesLeft):
    '''
    this function returns the number of misses left and lets
    the user know if they missed or not
    '''
#     lettersGuessed = guessedLetter
#     displayString = hangmanWord
#     guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
#     
    
    if guessedLetter in hangmanWord:
        return [missesLeft, True]
    else:
        missesLeft -= 1
        return [missesLeft, False]
# you still have this function, runGame, and DEBUG mode to do


def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    
    f = open(filename)
    data = f.readlines()
    words = []
    
    debugOrNot = handleUserInputDebugMode()
    DEBUG = debugOrNot
    
    wordLength = handleUserInputWordLength()
    wordWithLen = []

    
    for word in range(len(data)):
        words.append(data[word])
        if len(data[word]) == wordLength:
            wordWithLen.append(data[word])

    startingNum = handleUserInputDifficulty()
    missesLeft = startingNum
    #length = random.randint(5,11)
    
#     wordLength = handleUserInputWordLength()
    pick = list([word for word in words if len(word) == wordLength])
    indy = random.randint(0, len(wordWithLen)-1)
    word = wordWithLen[indy]
    leng = len(wordWithLen)
    #word = word(words, length-1)
    #word = words[0]
    hangmanWord = []
    secretWord = []
    lettersGuessed = []
    numOfGuesses = 0
    letterGuess = ''
    wordList = []
    currTemplate = ('_' * int(wordLength))
    newTemplate = currTemplate
    wordsWithLen2 = wordWithLen
    
    for char in word:
        hangmanWord.append("_")
        secretWord.append(char)
        
    hangmanWord.pop()
    while '_' in hangmanWord and (missesLeft > 0):
        indy = random.randint(0, len(wordWithLen)-1)
        lettersGuessed.sort()
        currTemplate = newTemplate
        wordWithLen = wordsWithLen2
        if DEBUG:
            print('(word is ' + str(word) + ')')
            print('# possible words: ' + str(len(wordsWithLen2)))
            #print('letter> ' + letterGuess)
            
        displayString = createDisplayString(lettersGuessed, missesLeft, hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        processing = processUserGuessClever(guessedLetter, word, missesLeft)
        letterGuess = guessedLetter
        
        if not processing[1]:
            print('you missed: ' + guessedLetter + ' not in word')
        
        (currTemplate, wordsWithLen2) = getNewWordList(currTemplate, letterGuess, wordWithLen, DEBUG)
        #word = pick[0]
        word = wordsWithLen2[random.randint(0, len(wordWithLen)-1)]
#         numOfGuesses += 1
#         lettersGuessed.append(guessedLetter)
        #print(newWord)
        #hangmanWord = newWord[0]
        missesLeft = processing[0]
        lettersGuessed.append(guessedLetter)
        
#         if processing[2] == False:
#             print("you missed: " + guessedLetter + " not in word")

    if missesLeft == 0:
        print("you're hung!!")
        print("word is " + word)
        if startingNum == 8:
            remainder = 8 - missesLeft
            print("you made " + str(numOfGuesses) + " guesses with " + str(remainder) + " misses")
        if startingNum == 12:
            remainder = 12 - missesLeft
            print("you made " + str(numOfGuesses) + " guesses with " + str(remainder) + " misses") 
        return False
    
    print("you guessed the word: " + word)
    if startingNum == 8:
        remainder = 8 - missesLeft
        print("you made " + str(numOfGuesses) + " guesses with " + str(remainder) + " misses")
    if startingNum == 12:
        remainder = 12 - missesLeft
        print("you made " + str(numOfGuesses) + " guesses with " + str(remainder) + " misses")
    return True  


if __name__ == "__maisn__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    
    wins = 0
    losses = 0
    decision = 'y'
    while decision == 'y':
        runGame2 = runGame('lowerwords.txt')
        if runGame2 == True:
            wins += 1
        else:
            losses += 1
        decision = input("Would you like to play again? y or n> ")
    
    print("You won " + str(wins) + " game(s) and lost " + str(losses))
    
    #print(createDisplayString(['b','e','u'], 4, 'um'))
    #print(createTemplate('tr__', 'u','true'))
    #print(getNewWordList('t___', 'u', ['true','trie','trup','turn','fdso','tupe','tunu'], True))
    
    
    
    
    