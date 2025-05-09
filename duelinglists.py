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

playerOne = random.sample(range(1,51), 10)
playerTwo = random.sample(range(1,51), 10)

print(f"Player One = {playerOne}")
print(f"Player Two = {playerTwo}")

oneWin = 0
twoWin = 0

for i in range(len(playerOne)):
    if playerOne[i] > playerTwo[i]:
        oneWin += 1
    elif playerOne[i] < playerTwo [i]:
        twoWin += 1

print(f"Player One won {oneWin} times.")
print(f"Player Two won {twoWin} times.")

oneHigh = max(playerOne)
twoHigh = max(playerTwo)
oneLow = min(playerOne)
twoLow = min(playerTwo)
oneHighIndex = playerOne.index(oneHigh)
twoHighIndex = playerTwo.index(twoHigh)
oneLowIndex = playerOne.index(oneLow)
twoLowIndex = playerTwo.index(twoLow)

print(f"Player One's highest number is {oneHigh} at index {oneHighIndex}.")
print(f"Player Two's highest number is {twoHigh} at index {twoHighIndex}.")
print(f"Player One's lowest number is {oneLow} at index {oneLowIndex}.")
print(f"Player Two's lowest number is {twoLow} at index {twoLowIndex}.")
