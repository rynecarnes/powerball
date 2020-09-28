import csv
import numpy as np
import matplotlib.pyplot as plt

inputfile = open('Powerball_1950-01-01_2020-09-23.csv', 'r')
myreader = csv.reader(inputfile)

winningNumbersList = []
firstNums = []
firstNumsOccurrences = {}
secondNums = []
secondNumsOccurrences = {}
thirdNums = []
thirdNumsOccurrences = {}
fourthNums = []
fourthNumsOccurrences = {}
fifthNums = []
fifthNumsOccurrences = {}
sixthNums = []
sixthNumsOccurrences = {}


for row in myreader:
    tempVal = row[1].split(' - ')
    tempVal.append(row[2])
    print(tempVal)
    winningNumbersList.append(tempVal)

winningNumbersList.pop(0)

for numList in winningNumbersList:
    firstNums.append(numList[0])
    secondNums.append(numList[1])
    thirdNums.append(numList[2])
    fourthNums.append(numList[3])
    fifthNums.append(numList[4])
    sixthNums.append(numList[5])

# print(winningNumbersList)
firstNumsSorted = [int(i) for i in firstNums]
firstNumsSorted.sort()

secondNumsSorted = [int(i) for i in secondNums]
secondNumsSorted.sort()

thirdNumsSorted = [int(i) for i in thirdNums]
thirdNumsSorted.sort()

fourthNumsSorted = [int(i) for i in fourthNums]
fourthNumsSorted.sort()

fifthNumsSorted = [int(i) for i in fifthNums]
fifthNumsSorted.sort()

sixthNumsSorted = [int(i) for i in sixthNums]
sixthNumsSorted.sort()

# Creating first number of occurrences dictionary
i = 0
num = firstNumsSorted[i]
count = 1

while i < len(firstNumsSorted) - 1:
    if firstNumsSorted[i + 1] == num:
        count = count + 1
    else:
        firstNumsOccurrences[num] = count
        num = firstNumsSorted[i + 1]
        count = 1
    i = i + 1

if firstNumsSorted[i] == num:
    firstNumsOccurrences[num] = count
else:
    firstNumsOccurrences[firstNumsSorted[i]] = 1

# Creating second number of occurrences dictionary
i = 0
num = secondNumsSorted[i]
count = 1

while i < len(secondNumsSorted) - 1:
    if secondNumsSorted[i + 1] == num:
        count = count + 1
    else:
        secondNumsOccurrences[num] = count
        num = secondNumsSorted[i + 1]
        count = 1
    i = i + 1

if secondNumsSorted[i] == num:
    secondNumsOccurrences[num] = count
else:
    secondNumsOccurrences[firstNumsSorted[i]] = 1


# Creating third number of occurrences dictionary
i = 0
num = thirdNumsSorted[i]
count = 1

while i < len(thirdNumsSorted) - 1:
    if thirdNumsSorted[i + 1] == num:
        count = count + 1
    else:
        thirdNumsOccurrences[num] = count
        num = thirdNumsSorted[i + 1]
        count = 1
    i = i + 1

if thirdNumsSorted[i] == num:
    thirdNumsOccurrences[num] = count
else:
    thirdNumsOccurrences[firstNumsSorted[i]] = 1


# Creating fourth number of occurrences dictionary
i = 0
num = fourthNumsSorted[i]
count = 1

while i < len(fourthNumsSorted) - 1:
    if fourthNumsSorted[i + 1] == num:
        count = count + 1
    else:
        fourthNumsOccurrences[num] = count
        num = fourthNumsSorted[i + 1]
        count = 1
    i = i + 1

if fourthNumsSorted[i] == num:
    fourthNumsOccurrences[num] = count
else:
    fourthNumsOccurrences[firstNumsSorted[i]] = 1


# Creating fifth number of occurrences dictionary
i = 0
num = fifthNumsSorted[i]
count = 1

while i < len(fifthNumsSorted) - 1:
    if fifthNumsSorted[i + 1] == num:
        count = count + 1
    else:
        fifthNumsOccurrences[num] = count
        num = fifthNumsSorted[i + 1]
        count = 1
    i = i + 1

if fifthNumsSorted[i] == num:
    fifthNumsOccurrences[num] = count
else:
    fifthNumsOccurrences[firstNumsSorted[i]] = 1

# Creating sixth number of occurrences dictionary
i = 0
num = sixthNumsSorted[i]
count = 1

while i < len(sixthNumsSorted) - 1:
    if sixthNumsSorted[i + 1] == num:
        count = count + 1
    else:
        sixthNumsOccurrences[num] = count
        num = sixthNumsSorted[i + 1]
        count = 1
    i = i + 1

if sixthNumsSorted[i] == num:
    sixthNumsOccurrences[num] = count
else:
    sixthNumsOccurrences[sixthNumsSorted[i]] = 1


# print("First Numbers:")
# print(firstNumsSorted)
# print("The First Number Position Occurrences:")
# for key, value in firstNumsOccurrences.items():
#     print(key, ': ', value)

firstSelectionNums = list(firstNumsOccurrences.keys())
firstSelectionOccurrences = list(firstNumsOccurrences.values())

fig = plt.figure(figsize=(20, 5))
plt.bar(firstSelectionNums, firstSelectionOccurrences, color='blue',
        width=0.4)
plt.xticks(np.arange(min(firstSelectionNums), max(firstSelectionNums)+1, 1.0))
plt.xlabel("Number Selected")
plt.ylabel("Times Number has been in Winning Drawing")
plt.title("Occurences of Winning Numbers for First Number Selection")
plt.show()

# print("Second Numbers:")
# print(secondNumsSorted)
# print("The Second Number Position Occurrences:")
# for key, value in secondNumsOccurrences.items():
#     print(key, ': ', value)

secondSelectionNums = list(secondNumsOccurrences.keys())
secondSelectionOccurrences = list(secondNumsOccurrences.values())

fig = plt.figure(figsize=(20, 5))
plt.bar(secondSelectionNums, secondSelectionOccurrences, color='red',
        width=0.4)
plt.xticks(np.arange(min(secondSelectionNums), max(secondSelectionNums)+1, 1.0))
plt.xlabel("Number Selected")
plt.ylabel("Times Number has been in Winning Drawing")
plt.title("Occurences of Winning Numbers for Second Number Selection")
plt.show()

# print("Third Numbers:")
# print(thirdNumsSorted)
# print("The Third Number Position Occurrences:")
# for key, value in thirdNumsOccurrences.items():
#     print(key, ': ', value)

thirdSelectionNums = list(thirdNumsOccurrences.keys())
thirdSelectionOccurrences = list(thirdNumsOccurrences.values())

fig = plt.figure(figsize=(20, 5))
plt.bar(thirdSelectionNums, thirdSelectionOccurrences, color='green',
        width=0.4)
plt.xticks(np.arange(min(thirdSelectionNums), max(thirdSelectionNums)+1, 1.0))
plt.xlabel("Number Selected")
plt.ylabel("Times Number has been in Winning Drawing")
plt.title("Occurences of Winning Numbers for Third Number Selection")
plt.show()

# print("Fourth Numbers:")
# print(fourthNumsSorted)
# print("The Fourth Number Position Occurrences:")
# for key, value in fourthNumsOccurrences.items():
#     print(key, ': ', value)

fourthSelectionNums = list(fourthNumsOccurrences.keys())
fourthSelectionOccurrences = list(fourthNumsOccurrences.values())

fig = plt.figure(figsize=(20, 5))
plt.bar(fourthSelectionNums, fourthSelectionOccurrences, color='purple',
        width=0.4)
plt.xticks(np.arange(min(fourthSelectionNums), max(fourthSelectionNums)+1, 1.0))
plt.xlabel("Number Selected")
plt.ylabel("Times Number has been in Winning Drawing")
plt.title("Occurences of Winning Numbers for Fourth Number Selection")
plt.show()

# print("Fifth Numbers:")
# print(fifthNumsSorted)
# print("The Fifth Number Position Occurrences:")
# for key, value in fifthNumsOccurrences.items():
#     print(key, ': ', value)

fifthSelectionNums = list(fifthNumsOccurrences.keys())
fifthSelectionOccurrences = list(fifthNumsOccurrences.values())

fig = plt.figure(figsize=(20, 5))
plt.bar(fifthSelectionNums, fifthSelectionOccurrences, color='black',
        width=0.4)
plt.xticks(np.arange(min(fifthSelectionNums), max(fifthSelectionNums)+1, 1.0))
plt.xlabel("Number Selected")
plt.ylabel("Times Number has been in Winning Drawing")
plt.title("Occurences of Winning Numbers for Fifth Number Selection")
plt.show()






sixthSelectionNums = list(sixthNumsOccurrences.keys())
sixthSelectionOccurrences = list(sixthNumsOccurrences.values())

fig = plt.figure(figsize=(20, 5))
plt.bar(sixthSelectionNums, sixthSelectionOccurrences, color='pink',
        width=0.4)
plt.xticks(np.arange(min(sixthSelectionNums), max(sixthSelectionNums)+1, 1.0))
plt.xlabel("Number Selected")
plt.ylabel("Times Number has been in Winning Drawing")
plt.title("Occurences of Winning Numbers for PowerBall")
plt.show()