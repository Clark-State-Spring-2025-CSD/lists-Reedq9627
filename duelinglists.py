#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

playerOne = []
playerTwo = []

for i in range(10):
    playerOne.append(random.randint(1, 50))
    playerTwo.append(random.randint(1, 50))
                     
playerOneWins = 0
playerTwoWins = 0

for i in range(10):
    if playerOne[i] > playerTwo[i]:
        playerOneWins += 1
    elif playerTwo[i] > playerOne[i]:
        playerTwoWins += 1

playerOneHigh = playerOne[0]
playerOneLow = playerOne[0]
playerOneHighIndex = 0
playerOneLowIndex = 0

for i in range(10):
    if playerOne[i] > playerOneHigh:
        playerOneHigh = playerOne[i]
        playerOneHighIndex = i
    if playerOne[i] < playerOneLow:
        playerOneLow = playerOne[i]
        playerOneLowIndex = i

playerTwoHigh = playerTwo[0]
playerTwoLow = playerTwo[0]
playerTwoHighIndex = 0
playerTwoLowIndex = 0

for i in range(10):
    if playerTwo[i] > playerTwoHigh:
        playerTwoHigh = playerTwo[i]
        playerTwoHighIndex = i
    if playerTwo[i] < playerTwoLow:
        playerTwoLow = playerTwo[i]
        playerTwoLowIndex = i

print("Player One's numbers:", playerOne)
print("Player Two's numbers:", playerTwo)
print ("Player One won", playerOneWins, "times.")
print("Player Two won", playerTwoWins, "times.")
print("Player One's highest number is", playerOneHigh, "at index", playerOneHighIndex)
print("Player Two's highest number is", playerTwoHigh, "at index", playerTwoHighIndex)
print("Player One's lowest number is", playerOneLow, "at index", playerOneLowIndex)
print("Player Two's lowest number is", playerTwoLow, "at index", playerTwoLowIndex)
